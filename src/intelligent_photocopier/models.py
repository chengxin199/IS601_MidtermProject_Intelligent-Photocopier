"""
Database models for Intelligent Photocopier.

Defines User and Course models with SQLAlchemy ORM.
"""

import os
from datetime import datetime, timezone

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    create_engine,
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Create base class for models
Base = declarative_base()


class User(Base):  # type: ignore[misc, valid-type]
    """User model for authentication and course ownership."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(80), unique=True, nullable=False, index=True)
    email = Column(String(120), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(200))
    bio = Column(Text)
    avatar_url = Column(String(500))
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # Relationship with courses
    courses = relationship("Course", back_populates="owner", cascade="all, delete-orphan")

    def to_dict(self, include_email: bool = False) -> dict:
        """Convert user to dictionary for JSON response."""
        data = {
            "id": self.id,
            "username": self.username,
            "full_name": self.full_name,
            "bio": self.bio,
            "avatar_url": self.avatar_url,
            "created_at": (
                self.created_at.isoformat() if self.created_at is not None else None  # type: ignore
            ),
        }
        if include_email:
            data["email"] = self.email
        return data


class Course(Base):  # type: ignore[misc, valid-type]
    """Course model for tracking generated courses."""

    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(String(100), unique=True, nullable=False, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    level = Column(String(50))  # beginner, intermediate, advanced
    duration = Column(String(50))  # e.g., "4 weeks"
    github_url = Column(String(500))
    deployed_url = Column(String(500))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # Nullable for anonymous
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # Relationship with user
    owner = relationship("User", back_populates="courses")

    def to_dict(self) -> dict:
        """Convert course to dictionary for JSON response."""
        return {
            "id": self.id,
            "course_id": self.course_id,
            "title": self.title,
            "description": self.description,
            "level": self.level,
            "duration": self.duration,
            "github_url": self.github_url,
            "deployed_url": self.deployed_url,
            "user_id": self.user_id,
            "created_at": (
                self.created_at.isoformat() if self.created_at is not None else None  # type: ignore
            ),
        }


# Database initialization
def get_database_url() -> str:
    """Get database URL from environment or use SQLite for development."""
    database_url = os.getenv("DATABASE_URL")

    if database_url:
        # Fix Heroku/Render postgres:// -> postgresql://
        if database_url.startswith("postgres://"):
            database_url = database_url.replace("postgres://", "postgresql://", 1)
        return database_url

    # Default to SQLite for local development
    return "sqlite:///./photocopier.db"


def init_db(database_url: str | None = None) -> tuple:
    """Initialize database and return engine and session factory."""
    db_url = database_url or get_database_url()

    # Create engine
    engine = create_engine(
        db_url,
        echo=False,  # Set to True for SQL debug logs
        pool_pre_ping=True,  # Verify connections before using
    )

    # Create all tables
    Base.metadata.create_all(engine)

    # Create session factory
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

    return engine, SessionLocal


def get_session(SessionLocal):
    """Get database session with automatic cleanup."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
