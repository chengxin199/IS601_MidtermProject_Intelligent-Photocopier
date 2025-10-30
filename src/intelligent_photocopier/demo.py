"""
Demo script for the Intelligent Photocopier.

This script demonstrates the complete course generation workflow
without requiring user input.
"""

import sys
from pathlib import Path

# Add the src directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from intelligent_photocopier.main import IntelligentPhotocopier


def demo_course_generation():
    """Demo the course generation with a sample course description."""
    
    # Sample course content that a user might paste
    sample_course_content = """
# B2: Performance Optimization and Profiling

Master the art of writing high-performance Python code that scales efficiently and runs lightning-fast.

This comprehensive course teaches you to identify bottlenecks, optimize algorithms, and implement efficient data structures. You'll learn profiling techniques, memory management, and parallel processing strategies used by top tech companies.

## Learning Objectives
- Profile Python applications to identify performance bottlenecks
- Optimize algorithms and choose efficient data structures
- Implement memory management and garbage collection strategies
- Apply caching and memoization techniques effectively
- Use parallel processing and async programming patterns
- Measure and validate performance improvements

## Topics Covered
- Performance profiling tools (cProfile, line_profiler, memory_profiler)
- Algorithm optimization and Big O analysis
- Data structure selection and optimization
- Memory management and object lifecycle
- Caching strategies (LRU, Redis, application-level)
- Concurrent and parallel programming
- Performance testing and benchmarking

Duration: 4-5 hours
Level: Intermediate
Prerequisites: 
- Solid Python programming experience
- Understanding of basic algorithms and data structures
- Familiarity with debugging tools
"""
    
    print("🎭 Intelligent Photocopier - Demo Mode")
    print("=" * 50)
    print()
    print("Sample course content:")
    print("-" * 30)
    print(sample_course_content[:200] + "..." if len(sample_course_content) > 200 else sample_course_content)
    print("-" * 30)
    print()
    
    # Initialize the photocopier
    photocopier = IntelligentPhotocopier("/home/chengxin199/myproject/code_quality_calc")
    
    # Generate the course
    success = photocopier.generate_course(sample_course_content)
    
    if success:
        print("\n🎉 Demo completed successfully!")
        print("Check the Lessons/ directory for the new B2-Performance-Optimization course.")
    else:
        print("\n❌ Demo failed. Check the error messages above.")


if __name__ == "__main__":
    demo_course_generation()