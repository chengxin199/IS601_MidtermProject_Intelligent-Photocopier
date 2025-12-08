"""
Tests for the Intelligent Photocopier API.

This module contains tests for authentication, course generation,
and user management endpoints.
"""

import json
from unittest.mock import MagicMock, patch

import pytest

from src.intelligent_photocopier.api import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_root_endpoint(client):
    """Test the root endpoint returns API information."""
    response = client.get("/")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["service"] == "Intelligent Photocopier API"
    assert data["status"] == "running"
    assert "version" in data


def test_health_endpoint(client):
    """Test the health check endpoint."""
    response = client.get("/api/health")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["status"] == "ok"


@patch("src.intelligent_photocopier.api.get_db")
def test_register_success(mock_db, client):
    """Test successful user registration."""
    # Mock database
    mock_session = MagicMock()
    mock_db.return_value = mock_session
    mock_session.query.return_value.filter.return_value.first.return_value = None

    # Mock the new user with proper ID
    mock_user = MagicMock()
    mock_user.id = 1
    mock_user.username = "testuser"
    mock_user.email = "test@example.com"

    def mock_refresh(user):
        user.id = 1
        user.username = "testuser"

    mock_session.refresh = mock_refresh

    payload = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "SecurePass123!",
    }

    response = client.post(
        "/api/auth/register", data=json.dumps(payload), content_type="application/json"
    )

    assert response.status_code == 201
    data = json.loads(response.data)
    assert data["message"] == "User registered successfully"
    assert "access_token" in data
    assert "user" in data


def test_register_missing_fields(client):
    """Test registration with missing required fields."""
    payload = {"username": "testuser"}

    response = client.post(
        "/api/auth/register", data=json.dumps(payload), content_type="application/json"
    )

    assert response.status_code == 400
    data = json.loads(response.data)
    assert "error" in data


@patch("src.intelligent_photocopier.api.get_db")
def test_login_invalid_credentials(mock_db, client):
    """Test login with invalid credentials."""
    # Mock database - user not found
    mock_session = MagicMock()
    mock_db.return_value = mock_session
    mock_session.query.return_value.filter.return_value.first.return_value = None

    payload = {"username": "nonexistent", "password": "wrongpass"}

    response = client.post(
        "/api/auth/login", data=json.dumps(payload), content_type="application/json"
    )

    assert response.status_code == 401
    data = json.loads(response.data)
    assert "error" in data


def test_generate_course_missing_fields(client):
    """Test course generation with missing required fields."""
    payload = {"title": "Test Course"}

    response = client.post(
        "/api/generate-course", data=json.dumps(payload), content_type="application/json"
    )

    assert response.status_code == 400
    data = json.loads(response.data)
    assert "error" in data
    assert "Missing required fields" in data["error"]


@patch("src.intelligent_photocopier.api.CourseGenerator")
@patch("src.intelligent_photocopier.api._commit_to_github")
def test_generate_course_success(mock_commit, mock_generator_class, client):
    """Test successful course generation."""
    # Mock course generator
    mock_generator = MagicMock()
    mock_generator_class.return_value = mock_generator
    mock_generator.generate_course_content.return_value = {
        "README.md": "# Test Course",
        "lesson-content.md": "## Lesson Content",
    }

    # Mock GitHub commit
    mock_commit.return_value = True

    payload = {
        "courseId": "test-course",
        "title": "Test Course",
        "content": "This is test content for the course.",
    }

    response = client.post(
        "/api/generate-course", data=json.dumps(payload), content_type="application/json"
    )

    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["success"] is True
    assert data["courseId"] == "test-course"
    assert "filesCreated" in data


def test_my_courses_unauthorized(client):
    """Test accessing my courses without authentication."""
    response = client.get("/api/courses/my")
    assert response.status_code == 401


@patch("src.intelligent_photocopier.api.get_db")
def test_admin_users_endpoint(mock_db, client):
    """Test admin users endpoint returns user list."""
    mock_session = MagicMock()
    mock_db.return_value = mock_session
    mock_session.query.return_value.order_by.return_value.all.return_value = []

    response = client.get("/api/admin/users")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "total" in data
    assert "users" in data


@patch("src.intelligent_photocopier.api.get_db")
def test_admin_stats_endpoint(mock_db, client):
    """Test admin stats endpoint returns statistics."""
    mock_session = MagicMock()
    mock_db.return_value = mock_session
    mock_session.query.return_value.count.return_value = 0
    mock_session.query.return_value.filter.return_value.count.return_value = 0

    response = client.get("/api/admin/stats")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "total_users" in data
    assert "total_courses" in data
