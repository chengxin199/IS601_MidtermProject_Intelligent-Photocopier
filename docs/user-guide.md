# User Guide: Intelligent Photocopier

## 🌐 Web Interface (Easiest Method)

**Visit**: [intelligentphotocopier.online](https://intelligentphotocopier.online)

### Quick Start - No Installation Required!

1. **Open your browser** (works on desktop, tablet, or phone)
2. **Visit** intelligentphotocopier.online
3. **Paste your course outline** in the text area
4. **Configure** course details (ID, title, level, duration)
5. **Click "Generate"** and wait ~2 minutes
6. **Preview instantly** - see your content right away
7. **Auto-deployed** - course goes live automatically

### Web Features
- ⚡ **Instant Preview** - View content immediately without waiting
- 📱 **Mobile Friendly** - Full responsive design for all devices
- 🚀 **Auto-Deploy** - Courses go live on Netlify automatically
- 📊 **Progress Tracking** - Live countdown and progress bar
- 🎨 **Modern UI** - Beautiful gradient design

---

## 💻 CLI Installation (For Developers)

### 1. Installation & Setup

**Prerequisites**:
- Python 3.11 or higher
- Git (for cloning the repository)
- OpenAI API key (optional for web, required for CLI)

**Installation Steps**:
```bash
# Clone the repository
git clone <repository-url>
cd code_quality_calc

# Set up development environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements-dev.txt

# Configure OpenAI API (optional)
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY=your_key_here
```

### 2. Verify Installation

Test that everything is working correctly:

```bash
# Run the test suite
python -m pytest tests/ -v

# Test the AI API (if configured)
python src/intelligent_photocopier/test_api.py

# Run a quick demo
python src/intelligent_photocopier/demo.py
```

## Using the Intelligent Photocopier

### Method 1: Interactive Mode (Recommended for Beginners)

The easiest way to get started:

```bash
python quickstart.py
```

**What you'll see**:
```
🎯 Intelligent Photocopier - Course Generator

Select an option:
1. Generate new course
2. View demo
3. Test API connection
4. Exit

Choice: 1

📝 Enter your course content (or course idea):
```

**Example Input**:
```
A2: DRY, Cohesion & Coupling, Clean Structure

Learning Objectives:
- Understand the DRY principle
- Learn about cohesion and coupling
- Practice clean code structure
```

**What happens next**:
1. ✅ Content analyzed successfully
2. ✅ Template structure extracted
3. ✅ AI content generated (7 files)
4. ✅ Course created: `Lessons/A2-dry-cohesion-coupling-clean-structure/`

### Method 2: Direct CLI Mode (For Advanced Users)

For direct command-line usage:

```bash
python -m src.intelligent_photocopier.main
```

**Input your course content** when prompted. The system accepts various formats:

**Format 1 - Standard Course Format**:
```
# A3: Advanced Testing Strategies

## Learning Objectives
- Master advanced testing techniques
- Implement test-driven development
- Create effective test suites

## Course Content
This course covers advanced testing methodologies...
```

**Format 2 - Simple Course Outline**:
```
B1 Database Design Principles [Advanced]

- Normalization techniques
- Index optimization
- Query performance tuning
```

**Format 3 - Informal Course Idea**:
```
Course: Introduction to Machine Learning

I want to create a course that teaches the basics of ML including:
- Linear regression
- Classification algorithms
- Model evaluation
```

### Method 3: Demo Mode (For Quick Preview)

See the system in action with pre-configured examples:

```bash
python src/intelligent_photocopier/demo.py
```

This runs through several example course generations automatically.

### Method 4: API Testing Mode

Test your OpenAI API configuration:

```bash
python src/intelligent_photocopier/test_api.py
```

## Understanding the Output

### Generated Course Structure

When you generate a course, you'll get a complete directory structure:

```
Lessons/A2-dry-cohesion-coupling-clean-structure/
├── README.md                           # 📚 Course overview
├── lesson-content.md                   # 📖 Detailed lesson content
├── summary.md                          # 📝 Key takeaways
├── reference/
│   ├── quick_reference.md             # ⚡ Quick reference guide
│   ├── best_practices.md              # 🏆 Industry best practices
│   └── exercise_instructions.md       # 💻 Hands-on exercises
└── solutions/
    └── practice_solution.py           # 🔧 Working code examples
```

### Content Quality

Each generated file contains:

**README.md**:
- 🎯 Clear learning objectives
- 📚 Course structure overview
- 🚀 Getting started instructions
- ⚡ Quick navigation links

**lesson-content.md**:
- 📖 Comprehensive educational content
- 💡 Practical examples
- 🔍 Detailed explanations
- 🎓 Progressive learning structure

**reference/quick_reference.md**:
- ⚡ Quick lookup information
- 📋 Key concepts summary
- 🔗 Essential links and resources

**reference/best_practices.md**:
- 🏆 Industry-standard practices
- ✅ Do's and don'ts
- 🎯 Professional recommendations

**reference/exercise_instructions.md**:
- 💻 Hands-on practice activities
- 🎯 Clear exercise objectives
- 📝 Step-by-step instructions

**solutions/practice_solution.py**:
- 🔧 Working code examples
- 💡 Implementation guidance
- 📝 Commented explanations

## Advanced Usage

### Custom Course Naming

The system automatically generates user-friendly directory names:

**Input**: `A2: DRY, Cohesion & Coupling, Clean Structure [Core]`
**Output**: `A2-dry-cohesion-coupling-clean-structure`

**Input**: `Advanced Database Optimization Techniques`
**Output**: `advanced-database-optimization-techniques`

### Multiple Course Generation

Generate multiple courses in a session:

```bash
python quickstart.py
# Choose option 1 for each course you want to create
```

Each course gets its own directory with complete content.

### Working Without AI

The system works even without an OpenAI API key:

1. **Placeholder Mode**: Generates structured placeholder content
2. **Template-Based**: Uses the A1-Defensive-Programming structure
3. **Professional Format**: Maintains consistent formatting and structure

**Example without API**:
```bash
# Don't set OPENAI_API_KEY in .env
python quickstart.py
```

You'll get complete course structures with placeholder content that you can manually edit.

## Configuration Options

### Environment Variables

Create a `.env` file in the project root:

```bash
# OpenAI Configuration
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini

# Path Configuration
LESSONS_PATH=Lessons
TEMPLATE_PATH=Lessons/A1-Defensive-Programming

# AI Generation Settings
MAX_TOKENS=2000
TEMPERATURE=0.7
```

### Customizing Output Location

Change where courses are created:

```bash
# In .env file
LESSONS_PATH=MyCustomCourses
```

### AI Model Selection

Use different OpenAI models:

```bash
# In .env file
OPENAI_MODEL=gpt-4           # More powerful, more expensive
OPENAI_MODEL=gpt-3.5-turbo   # Faster, less expensive
OPENAI_MODEL=gpt-4o-mini     # Default, balanced option
```

## Troubleshooting

### Common Issues

**1. "No module named 'openai'"**
```bash
# Solution: Install dependencies
pip install -r requirements-dev.txt
```

**2. "API key not found"**
```bash
# Solution: Check your .env file
cat .env
# Make sure OPENAI_API_KEY=your_actual_key_here
```

**3. "Permission denied" when creating files**
```bash
# Solution: Check directory permissions
chmod 755 Lessons/
```

**4. "Template not found"**
```bash
# Solution: Ensure A1-Defensive-Programming exists
ls -la Lessons/A1-Defensive-Programming/
```

### Debugging Mode

Enable detailed logging:

```bash
# Run with debug output
python -c "
import logging
logging.basicConfig(level=logging.DEBUG)
import src.intelligent_photocopier.main as main
"
```

### API Connection Issues

Test your API connection:

```bash
python src/intelligent_photocopier/test_api.py
```

**Expected output**:
```
✅ OpenAI API connection successful
✅ Content generation test passed
✅ All systems operational
```

### File System Issues

Check file system permissions:

```bash
# Verify you can create directories
mkdir -p test_directory/subdirectory
touch test_directory/test_file.txt
rm -rf test_directory
```

## Tips for Best Results

### 1. Input Format Tips

**For best AI generation quality**:

✅ **Good Input**:
```
A2: Advanced Python Testing

Learning Objectives:
- Master pytest framework
- Implement test-driven development
- Create comprehensive test suites
- Understand mocking and fixtures

This course teaches advanced Python testing techniques including...
```

❌ **Less Optimal Input**:
```
testing
```

### 2. Course Naming Conventions

**Recommended naming patterns**:
- `A1`, `A2`, `A3` - Beginner level
- `B1`, `B2`, `B3` - Intermediate level
- `C1`, `C2`, `C3` - Advanced level

**Examples**:
- `A1: Introduction to Python`
- `B2: Advanced Web Development`
- `C3: Machine Learning Engineering`

### 3. Content Structure Tips

**Include these elements for best results**:
- Clear learning objectives
- Prerequisites (if any)
- Expected outcomes
- Course context or motivation

### 4. Iterative Improvement

**Refine generated content**:
1. Generate initial course structure
2. Review and edit the generated content
3. Use successful courses as templates for similar topics
4. Build a library of high-quality courses

## Integration with Development Workflow

### VS Code Integration

**Recommended extensions**:
- Python extension pack
- Markdown preview
- File tree view
- Git integration

**Open generated courses**:
```bash
code Lessons/A2-dry-cohesion-coupling-clean-structure/
```

### Git Integration

**Track course versions**:
```bash
git add Lessons/
git commit -m "Add A2: DRY, Cohesion & Coupling course"
git push
```

### Automated Workflows

**Create course generation scripts**:
```bash
#!/bin/bash
# generate_course.sh

echo "Course title: $1"
echo "$1" | python -m src.intelligent_photocopier.main
echo "Course generated successfully!"
```

**Usage**:
```bash
./generate_course.sh "A3: Advanced Design Patterns"
```

## Examples and Use Cases

### Use Case 1: Programming Course Series

**Goal**: Create a comprehensive Python programming series

**Approach**:
```bash
# Generate foundation courses
echo "A1: Python Basics and Syntax" | python -m src.intelligent_photocopier.main
echo "A2: Control Flow and Functions" | python -m src.intelligent_photocopier.main
echo "A3: Data Structures and Algorithms" | python -m src.intelligent_photocopier.main

# Generate intermediate courses
echo "B1: Object-Oriented Programming" | python -m src.intelligent_photocopier.main
echo "B2: Advanced Python Features" | python -m src.intelligent_photocopier.main
echo "B3: Testing and Debugging" | python -m src.intelligent_photocopier.main
```

### Use Case 2: Corporate Training

**Goal**: Create standardized training materials for a development team

**Approach**:
1. Define company coding standards
2. Generate courses covering team practices
3. Include company-specific examples
4. Maintain consistent quality across all materials

### Use Case 3: Educational Institution

**Goal**: Rapidly prototype course content for curriculum development

**Approach**:
1. Generate initial course structures
2. Review and refine content with subject matter experts
3. Adapt content for specific student populations
4. Maintain version control for curriculum updates

## Support and Community

### Getting Help

**1. Check Documentation**:
- `docs/` directory contains comprehensive guides
- README.md has quick start information
- `docs/troubleshooting.md` for common issues

**2. Review Code Examples**:
- `src/intelligent_photocopier/demo.py` - Working examples
- `tests/` directory - Test cases and usage patterns
- Generated courses for content examples

**3. Debug Information**:
- Enable debug logging for detailed information
- Check log files for error details
- Use test scripts to isolate issues

### Contributing

**Improve the system**:
1. Report bugs and issues
2. Suggest new features
3. Contribute code improvements
4. Share successful course examples

**Development workflow**:
```bash
# Set up development environment
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt

# Run quality checks
python -m pytest tests/ -v
python -m flake8 src/
python -m mypy src/
```

This user guide should help you get the most out of the Intelligent Photocopier system. Remember that the AI-generated content is a starting point - you can always edit and refine the generated courses to meet your specific needs.
