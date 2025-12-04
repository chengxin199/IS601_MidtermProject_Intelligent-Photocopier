"""
Course generator for the Intelligent Photocopier.

This module handles the generation of course content using AI or fallback templates.
"""

import logging
from datetime import datetime
from typing import Any, Dict

from .config import config

try:
    from openai import OpenAI

    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    OpenAI = type(None)  # type: ignore  # Type placeholder for when OpenAI is not available


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CourseGenerator:
    """Generates course content using OpenAI API based on templates and user input."""

    def __init__(self, api_key: str | None = None):
        """Initialize the course generator with optional API key."""
        self.api_key = api_key or config.openai_api_key
        if OPENAI_AVAILABLE:
            self.client = self._initialize_client() if self.api_key else None
        else:
            self.client = None

    @staticmethod
    def _create_front_matter(
        title: str,
        layout: str = "layouts/course.njk",
        **metadata,
    ) -> str:
        """Create YAML front matter for Eleventy.

        Args:
            title: Page title
            layout: Layout template path
            **metadata: Additional metadata (course_id, level, duration, description, tags)
        """
        front_matter = ["---", f"title: {title}", f"layout: {layout}"]

        if course_id := metadata.get("course_id"):
            front_matter.append(f"courseId: {course_id}")
        if level := metadata.get("level"):
            front_matter.append(f"level: {level}")
        if duration := metadata.get("duration"):
            front_matter.append(f"duration: {duration}")
        if description := metadata.get("description"):
            # Escape quotes in description
            clean_desc = description.replace('"', '\\"')
            front_matter.append(f'description: "{clean_desc}"')
        if tags := metadata.get("tags"):
            front_matter.append("tags:")
            for tag in tags:
                front_matter.append(f"  - {tag}")

        # Add date
        front_matter.append(f"date: {datetime.now().isoformat()}")

        front_matter.append("---\n")
        return "\n".join(front_matter)

    def _initialize_client(self):
        """Initialize OpenAI client."""
        if not OPENAI_AVAILABLE:
            logger.warning("OpenAI library not available")
            return None

        if not self.api_key:
            logger.warning("No OpenAI API key provided")
            return None

        try:
            from openai import OpenAI

            client = OpenAI(api_key=self.api_key)
            logger.info("OpenAI client initialized successfully")
            return client
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI client: {e}")
            return None

    def generate_course_content(
        self, course_info: Dict[str, Any], template_structure: Dict[str, Any]
    ) -> Dict[str, str]:
        """Generate complete course content based on info and template."""
        if not self.client:
            logger.warning("No OpenAI client available - generating placeholder content")
            return self._generate_placeholder_content(course_info)

        try:
            logger.info(f"Generating AI content for course: {course_info['title']}")

            # Generate each type of content
            content = {}

            # Generate README.md
            content["README.md"] = self._generate_ai_readme(course_info, template_structure)

            # Generate lesson-content.md
            content["lesson-content.md"] = self._generate_ai_lesson_content(
                course_info, template_structure
            )

            # Generate summary.md
            content["summary.md"] = self._generate_ai_summary(course_info, template_structure)

            # Generate reference materials
            content["reference/quick_reference.md"] = self._generate_ai_quick_reference(course_info)
            content["reference/best_practices.md"] = self._generate_ai_best_practices(course_info)
            content["reference/exercise_instructions.md"] = self._generate_ai_exercise_instructions(
                course_info
            )

            # Generate solutions (Markdown format for better documentation)
            content["solutions/practice_solution.md"] = self._generate_ai_practice_solution(
                course_info
            )

            logger.info("AI content generation completed successfully")
            return content

        except Exception as e:
            logger.error(f"AI content generation failed: {e}")
            logger.info("Falling back to placeholder content")
            return self._generate_placeholder_content(course_info)

    def _generate_ai_readme(
        self, course_info: Dict[str, Any], template_structure: Dict[str, Any]
    ) -> str:
        """Generate README.md using AI."""

        prompt = f"""Create a comprehensive course README.md for a programming lesson about "{course_info['title']}".

Course Details:
- Title: {course_info['title']}
- Duration: {course_info['duration']}
- Level: {course_info['level']}
- Description: {course_info['description']}
- Learning Objectives: {', '.join(course_info['objectives'])}
- Prerequisites: {', '.join(course_info['prerequisites'])}

Requirements:
1. Follow this EXACT structure and format:
   - Course title with emoji
   - Course Overview section with duration and level
   - Learning Objectives (bulleted list)
   - Topics Covered (bulleted list)
   - Prerequisites (bulleted list)
   - Folder Structure (ASCII tree format)
   - Learning Path (numbered steps)
   - Assessment Criteria
   - Common Pitfalls to Avoid
   - Reflection Questions

2. Use engaging emojis like 🎯 📚 🚀 ⚡ 💻 🔧
3. Make it professional but approachable
4. Include practical, actionable content
5. End with motivational call-to-action

Generate a complete, professional README that matches the style of high-quality educational content."""

        try:
            if not self.client:
                raise ValueError("OpenAI client not initialized")

            response = self.client.chat.completions.create(
                model=config.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert educational content creator specializing in programming courses. Create clear, engaging, and professionally structured course materials.",
                    },
                    {"role": "user", "content": prompt},
                ],
                max_tokens=config.max_tokens,
                temperature=config.temperature,
            )

            content = response.choices[0].message.content
            markdown_content = content.strip() if content else ""

            # Add front matter for Eleventy
            front_matter = self._create_front_matter(
                title=course_info["title"],
                layout="layouts/course.njk",
                course_id=course_info.get("course_id"),
                level=course_info.get("level"),
                duration=course_info.get("duration"),
                description=course_info.get("description"),
                tags=["course", "programming", course_info.get("level", "").lower()],
            )

            return front_matter + markdown_content

        except Exception as e:
            logger.error(f"Failed to generate AI README: {e}")
            return self._generate_readme(course_info)

    def _generate_ai_lesson_content(
        self, course_info: Dict[str, Any], template_structure: Dict[str, Any]
    ) -> str:
        """Generate lesson-content.md using AI."""

        prompt = f"""Create comprehensive lesson content for a programming course about "{course_info['title']}".

Course Details:
- Title: {course_info['title']}
- Duration: {course_info['duration']}
- Level: {course_info['level']}
- Description: {course_info['description']}
- Learning Objectives: {', '.join(course_info['objectives'])}

Requirements:
1. Structure as multiple modules (3-5 modules):
   - Module 1: Introduction and Fundamentals
   - Module 2: Core Concepts and Theory
   - Module 3: Practical Implementation
   - Module 4: Advanced Techniques
   - Module 5: Best Practices and Patterns

2. Each module should include:
   - Clear learning goals
   - Theoretical explanations
   - Code examples in Python
   - Practical exercises
   - Real-world applications

3. Include:
   - Detailed code snippets with explanations
   - Best practices and patterns
   - Common pitfalls and how to avoid them
   - Performance considerations
   - Security implications (if relevant)

4. Use markdown formatting with:
   - Clear headers
   - Code blocks with syntax highlighting
   - Bullet points and numbered lists
   - Emphasis for key concepts

5. Make it comprehensive but digestible - suitable for {course_info['duration']} of learning.

Generate professional, technical content that teaches the subject thoroughly."""

        try:
            if not self.client:
                raise ValueError("OpenAI client not initialized")

            response = self.client.chat.completions.create(
                model=config.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert programming instructor with deep knowledge of software development best practices. Create detailed, technical educational content with practical examples.",
                    },
                    {"role": "user", "content": prompt},
                ],
                max_tokens=3000,  # Longer content for lesson material
                temperature=0.6,  # Slightly more focused for technical content
            )

            content = response.choices[0].message.content
            markdown_content = content.strip() if content else ""

            # Add front matter for Eleventy
            front_matter = self._create_front_matter(
                title=f"{course_info['title']} - Detailed Lessons",
                layout="layouts/course.njk",
                course_id=course_info.get("course_id"),
                level=course_info.get("level"),
                duration=course_info.get("duration"),
                tags=["lesson", "content", course_info.get("level", "").lower()],
            )

            return front_matter + markdown_content

        except Exception as e:
            logger.error(f"Failed to generate AI lesson content: {e}")
            return self._generate_lesson_content(course_info)

    def _generate_ai_summary(
        self, course_info: Dict[str, Any], template_structure: Dict[str, Any]
    ) -> str:
        """Generate summary.md using AI."""

        prompt = f"""Create a comprehensive lesson summary for a programming course about "{course_info['title']}".

Course Details:
- Title: {course_info['title']}
- Learning Objectives: {', '.join(course_info['objectives'])}
- Level: {course_info['level']}

Requirements:
1. Structure with these sections:
   - 🎯 Learning Objectives Achieved (checkboxes)
   - 📚 Key Concepts Mastered (detailed explanations)
   - 🛠️ Practical Skills Applied (what students can now do)
   - 🔍 Common Pitfalls Avoided (what to watch out for)
   - 📈 Quality Metrics Improved (measurable improvements)
   - 🚀 Next Steps & Advanced Topics
   - 💡 Key Takeaways (memorable insights)
   - 🎓 Assessment Checklist (self-evaluation)

2. Use emojis consistently and appropriately
3. Include specific, actionable takeaways
4. Provide clear assessment criteria
5. Suggest concrete next steps for continued learning
6. Make it motivational and encouraging

Generate a comprehensive summary that helps students consolidate their learning and plan next steps."""

        try:
            if not self.client:
                raise ValueError("OpenAI client not initialized")

            response = self.client.chat.completions.create(
                model=config.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert educational designer who creates effective learning summaries and assessments. Focus on concrete outcomes and practical applications.",
                    },
                    {"role": "user", "content": prompt},
                ],
                max_tokens=config.max_tokens,
                temperature=config.temperature,
            )

            content = response.choices[0].message.content
            markdown_content = content.strip() if content else ""

            # Add front matter for Eleventy
            front_matter = self._create_front_matter(
                title=f"{course_info['title']} - Summary",
                layout="layouts/course.njk",
                course_id=course_info.get("course_id"),
                level=course_info.get("level"),
                tags=["summary", "assessment", course_info.get("level", "").lower()],
            )

            return front_matter + markdown_content

        except Exception as e:
            logger.error(f"Failed to generate AI summary: {e}")
            return self._generate_summary(course_info)

    def _generate_placeholder_content(self, course_info: Dict[str, Any]) -> Dict[str, str]:
        """Generate placeholder content when AI is not available."""
        return {
            "README.md": self._generate_readme(course_info),
            "lesson-content.md": self._generate_lesson_content(course_info),
            "summary.md": self._generate_summary(course_info),
        }

    def _generate_readme(self, course_info: Dict[str, Any]) -> str:
        """Generate README.md content."""
        topics_section = ""
        if course_info.get("topics"):
            topics_list = chr(10).join([f"- {topic}" for topic in course_info["topics"]])
            topics_section = f"""## Topics Covered
{topics_list}

"""

        return f"""# {course_info['course_id']}: {course_info['title']}

## Course Overview
**Duration**: {course_info['duration']} | **Level**: {course_info['level']}

{course_info['description']}

## Learning Objectives
By the end of this lesson, you will be able to:
{chr(10).join([f"- {obj}" for obj in course_info['objectives']])}

{topics_section}## Prerequisites
{chr(10).join([f"- {prereq}" for prereq in course_info['prerequisites']])}

## Folder Structure
```
{course_info['course_id']}/
├── README.md                    # This overview
├── lesson-content.md           # Detailed lesson material
├── summary.md                  # Key takeaways and assessment
├── tests/                      # Practice exercises and tests
├── solutions/                  # Reference solutions
└── reference/                  # Learning resources
```

## Learning Path
1. **Read** `lesson-content.md` for comprehensive theory
2. **Practice** with exercises in `tests/` directory
3. **Review** solutions and references
4. **Assess** your learning with `summary.md`

**Ready to start?** Open `lesson-content.md` and begin your journey! 🚀
"""

    def _generate_lesson_content(self, course_info: Dict[str, Any]) -> str:
        """Generate lesson-content.md content."""
        return f"""# Lesson Content: {course_info['title']}

## Module 1: Introduction (45 minutes)

### 1.1 Overview
This lesson covers {course_info['title'].lower()} with a focus on practical application.

{course_info['description']}

### 1.2 Learning Objectives
{chr(10).join([f"- {obj}" for obj in course_info['objectives']])}

## Module 2: Core Concepts (60 minutes)

### 2.1 Fundamental Principles
// TODO: AI will generate detailed content based on the course topic

### 2.2 Best Practices
// TODO: AI will generate best practices specific to the topic

## Module 3: Practical Application (90 minutes)

### 3.1 Hands-on Examples
// TODO: AI will generate code examples and exercises

### 3.2 Common Patterns
// TODO: AI will generate common implementation patterns

## Hands-on Exercise Overview
Practice these concepts with the exercises in the `tests/` folder.

Ready to start practicing? Head to the practice exercises!
"""

    def _generate_summary(self, course_info: Dict[str, Any]) -> str:
        """Generate summary.md content."""
        return f"""# Lesson Summary: {course_info['title']}

## 🎯 Learning Objectives Achieved

By completing this lesson, you should now be able to:

{chr(10).join([f"- ✅ **{obj}**" for obj in course_info['objectives']])}

## 📚 Key Concepts Mastered

// TODO: AI will generate detailed summary based on course content

## 🎓 Assessment Checklist

Mark your understanding level for each concept:

**Core Concepts**
{chr(10).join([f"- [ ] {obj}" for obj in course_info['objectives'][:3]])}

**Practical Skills**
{chr(10).join([f"- [ ] {obj}" for obj in course_info['objectives'][3:]])}

## 🚀 Next Steps

1. **Apply to projects**: Use these skills in real applications
2. **Explore advanced topics**: Dive deeper into specialized areas
3. **Share knowledge**: Teach others what you've learned

**Congratulations!** You've completed the {course_info['title']} lesson.
"""

    def _generate_ai_quick_reference(self, course_info: Dict[str, Any]) -> str:
        """Generate quick reference using AI."""
        if not self.client:
            return f"# {course_info['title']} - Quick Reference\n\n// TODO: Add quick reference content"

        prompt = f"""Create a comprehensive quick reference guide for "{course_info['title']}".

Course Overview:
- Duration: {course_info['duration']}
- Level: {course_info['level']}
- Topics: {', '.join(course_info.get('topics', []))}

Requirements:
1. Key concepts with brief explanations
2. Common patterns and syntax examples
3. Code snippets where relevant
4. Troubleshooting quick fixes
5. Use clear formatting with headers and bullet points

Generate a practical quick reference that students can use during coding."""

        try:
            if not self.client:
                raise ValueError("OpenAI client not initialized")

            response = self.client.chat.completions.create(
                model=config.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert technical writer creating practical reference materials. Focus on actionable, concise information.",
                    },
                    {"role": "user", "content": prompt},
                ],
                max_tokens=1500,
                temperature=0.5,
            )

            content = response.choices[0].message.content

            # Add front matter
            if content:
                markdown_content = content.strip()
                front_matter = self._create_front_matter(
                    title=f"{course_info['title']} - Quick Reference",
                    layout="layouts/course.njk",
                    course_id=course_info.get("course_id"),
                    tags=["reference", "quick-guide"],
                )
                return front_matter + markdown_content
            return self._generate_placeholder_quick_reference(course_info)

        except Exception as e:
            logger.error(f"Failed to generate AI quick reference: {e}")
            return self._generate_placeholder_quick_reference(course_info)

    def _generate_ai_best_practices(self, course_info: Dict[str, Any]) -> str:
        """Generate best practices using AI."""
        if not self.client:
            return (
                f"# {course_info['title']} - Best Practices\n\n// TODO: Add best practices content"
            )

        prompt = f"""Create a comprehensive best practices guide for "{course_info['title']}".

Generate best practices covering:
1. Core principles and guidelines
2. Common pitfalls to avoid
3. Performance considerations
4. Security considerations (if applicable)
5. Testing strategies
6. Code organization tips

Make it practical and actionable for {course_info['level'].lower()} level developers."""

        try:
            if not self.client:
                raise ValueError("OpenAI client not initialized")

            response = self.client.chat.completions.create(
                model=config.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert software architect providing practical guidance. Focus on actionable best practices.",
                    },
                    {"role": "user", "content": prompt},
                ],
                max_tokens=2000,
                temperature=0.6,
            )

            content = response.choices[0].message.content

            # Add front matter
            if content:
                markdown_content = content.strip()
                front_matter = self._create_front_matter(
                    title=f"{course_info['title']} - Best Practices",
                    layout="layouts/course.njk",
                    course_id=course_info.get("course_id"),
                    tags=["best-practices", "guidelines"],
                )
                return front_matter + markdown_content
            return self._generate_placeholder_best_practices(course_info)

        except Exception as e:
            logger.error(f"Failed to generate AI best practices: {e}")
            return self._generate_placeholder_best_practices(course_info)

    def _generate_ai_exercise_instructions(self, course_info: Dict[str, Any]) -> str:
        """Generate exercise instructions using AI."""
        if not self.client:
            return f"# {course_info['title']} - Exercise Instructions\n\n// TODO: Add exercise instructions"

        prompt = f"""Create detailed hands-on coding exercise instructions for "{course_info['title']}".

Learning Objectives:
{chr(10).join([f"- {obj}" for obj in course_info['objectives']])}

Create 3-5 progressive coding exercises that:
1. **Include starter code** - Provide Python code templates with TODO comments
2. **Have clear objectives** - State what the student should implement
3. **Build incrementally** - Start simple, add complexity
4. **Include test cases** - Show expected input/output examples
5. **Provide hints** - Give helpful tips for common challenges

Format each exercise as:

## Exercise [N]: [Title]
**Difficulty:** [Beginner/Intermediate/Advanced]
**Time Estimate:** [X minutes]

### Objective
Clear description of what to implement

### Starter Code
```python
# Provide actual code template with TODO markers
def function_name():
    # TODO: Implement this
    pass
```

### Requirements
- Specific requirement 1
- Specific requirement 2
- Include edge cases to handle

### Test Cases
```python
# Example test cases
assert function_name(input1) == expected_output1
assert function_name(input2) == expected_output2
```

### Hints
- Helpful hint 1
- Helpful hint 2

Generate practical, code-focused exercises suitable for {course_info['level'].lower()} level."""

        try:
            if not self.client:
                raise ValueError("OpenAI client not initialized")

            response = self.client.chat.completions.create(
                model=config.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert Python instructor creating hands-on coding exercises. Focus on providing actual runnable code templates and clear test cases.",
                    },
                    {"role": "user", "content": prompt},
                ],
                max_tokens=config.max_tokens,
                temperature=config.temperature,
            )

            content = response.choices[0].message.content

            # Add front matter
            if content:
                markdown_content = content.strip()
                front_matter = self._create_front_matter(
                    title=f"{course_info['title']} - Exercise Instructions",
                    layout="layouts/course.njk",
                    course_id=course_info.get("course_id"),
                    tags=["exercises", "practice"],
                )
                return front_matter + markdown_content
            return self._generate_placeholder_exercise_instructions(course_info)

        except Exception as e:
            logger.error(f"Failed to generate AI exercise instructions: {e}")
            return self._generate_placeholder_exercise_instructions(course_info)

    def _generate_ai_practice_solution(self, course_info: Dict[str, Any]) -> str:
        """Generate practice solution using AI in Markdown format."""
        if not self.client:
            return f"# {course_info['title']} - Practice Solution\n\n## TODO\nAdd practice solution code"

        objectives_text = chr(10).join([f"- {obj}" for obj in course_info['objectives']])
        prompt = f"""Create a comprehensive practice solution document in Markdown format for "{course_info['title']}".

Learning Objectives to demonstrate:
{objectives_text}

For each exercise from the exercise instructions, provide:
1. **Complete working code** - Fully functional implementation
2. **Progressive solutions** - Basic version, then enhanced version with proper error handling
3. **Detailed inline comments** - Explain key logic step-by-step
4. **Testing examples** - Show how to test the code with test cases
5. **Alternative approaches** - Demonstrate different implementation strategies

Format each solution with these sections:
- Overview: Brief description of the solution approach
- Basic Implementation: Clean working code with comments
- Enhanced Implementation: Improved version with error handling and validation
- Testing the Solution: Complete test cases with assertions
- Explanation: Design decisions, key concepts, complexity analysis
- Key Takeaways: Important lessons and best practices

Use proper Markdown formatting with code blocks (use triple backticks with python).
Include inline comments explaining each step.
Show both basic and enhanced versions with proper error handling.
Provide runnable test cases that demonstrate the solution works.

Generate production-quality, well-tested solutions for {course_info['level'].lower()} level."""

        try:
            if not self.client:
                raise ValueError("OpenAI client not initialized")

            response = self.client.chat.completions.create(
                model=config.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a senior Python engineer and instructor. Provide clean, production-quality code with comprehensive explanations, proper error handling, and complete testing examples. Focus on real-world applicability.",
                    },
                    {"role": "user", "content": prompt},
                ],
                max_tokens=config.max_tokens,
                temperature=config.temperature,
            )

            content = response.choices[0].message.content

            # Add front matter
            if content:
                markdown_content = content.strip()
                front_matter = self._create_front_matter(
                    title=f"{course_info['title']} - Practice Solution",
                    layout="layouts/course.njk",
                    course_id=course_info.get("course_id"),
                    tags=["solutions", "code"],
                )
                return front_matter + markdown_content
            return self._generate_placeholder_practice_solution(course_info)

        except Exception as e:
            logger.error(f"Failed to generate AI practice solution: {e}")
            return self._generate_placeholder_practice_solution(course_info)

    def _generate_placeholder_quick_reference(self, course_info: Dict[str, Any]) -> str:
        """Generate placeholder quick reference."""
        return f"""# {course_info['title']} - Quick Reference

## Key Concepts
// TODO: Add key concepts for {course_info['title']}

## Common Patterns
// TODO: Add common implementation patterns

## Best Practices
// TODO: Add best practices

## Troubleshooting
// TODO: Add troubleshooting tips
"""

    def _generate_placeholder_best_practices(self, course_info: Dict[str, Any]) -> str:
        """Generate placeholder best practices."""
        return f"""# {course_info['title']} - Best Practices

## Core Principles
// TODO: Add core principles for {course_info['title']}

## Common Pitfalls
// TODO: Add common pitfalls to avoid

## Performance Tips
// TODO: Add performance considerations
"""

    def _generate_placeholder_exercise_instructions(self, course_info: Dict[str, Any]) -> str:
        """Generate placeholder exercise instructions."""
        return f"""# {course_info['title']} - Exercise Instructions

## Exercise 1: Basic Implementation
// TODO: Add detailed exercise instructions

## Exercise 2: Intermediate Practice
// TODO: Add intermediate exercise

## Exercise 3: Advanced Challenge
// TODO: Add advanced exercise
"""

    def _generate_placeholder_practice_solution(self, course_info: Dict[str, Any]) -> str:
        """Generate placeholder practice solution in Markdown format."""
        return f'''# Practice Solution - {course_info['title']}

## Overview
This document demonstrates the key concepts covered in the lesson.

## Learning Objectives
{chr(10).join([f"- {obj}" for obj in course_info['objectives']])}

## Solution 1: Basic Implementation

```python
"""
{course_info['title']} - Basic Solution

This example demonstrates the core concepts.
"""

def main():
    """Main function demonstrating key concepts."""
    print("Practice solution for {course_info['title']}")
    # TODO: Add implementation
    pass

if __name__ == "__main__":
    main()
```

## Explanation
// TODO: Add detailed explanation of the solution approach

## Key Takeaways
// TODO: Add important points learned from this solution

## Next Steps
// TODO: Suggest how to extend or improve this solution
'''
