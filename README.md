![CI](https://github.com/chengxin199/IS601_MidtermProject_Intelligent-Photocopier/actions/workflows/quality.yml/badge.svg?branch=main)

# 🤖 Intelligent Photocopier — AI-Powered Course Generator

> **Transform programming education with AI-generated courses** that create comprehensive, professional-grade learning materials from simple course outlines.

The **Intelligent Photocopier** is an advanced AI-powered system that generates complete programming courses automatically. Using OpenAI gpt-4.1-mini and sophisticated template analysis, it creates professional educational content with the same quality and structure as industry-standard training materials.

## 🌐 Live Web App

**Visit**: [intelligentphotocopier.online](https://intelligentphotocopier.online)

**New Features (December 2025)**:
- ⚡ **Instant Preview** — View generated courses immediately without waiting for deployment
- 📱 **Mobile Responsive** — Full support for phones and tablets with optimized touch interfaces
- 🚀 **Batch Git Commits** — All course files committed in a single transaction
- ⏱️ **Deployment Countdown** — Live progress tracking for Netlify deployments
- 🎨 **Modern UI/UX** — Beautiful gradient design with smooth animations

## 🎯 What the Intelligent Photocopier Does

**Input**: A simple course outline or description
**Output**: A complete, professional programming course with:

- 📚 **Comprehensive README** with course overview and learning objectives
- 📖 **Detailed lesson content** with explanations, examples, and best practices
- 📋 **Quick reference guides** and cheat sheets
- 💻 **Working code examples** and practice solutions
- 🧪 **Exercise instructions** with step-by-step guidance
- 📝 **Course summaries** and assessment materials

## ⚡ Quick Start Guide

### **Method 1: Web Interface (Easiest)** 🆕
**Visit**: [intelligentphotocopier.online](https://intelligentphotocopier.online)

1. **Paste your course outline** or upload a file
2. **Configure course details** (ID, title, level, duration)
3. **Click Generate** — AI creates your course in ~2 minutes
4. **Preview Instantly** — View content immediately
5. **Auto-Deploy** — Course goes live on Netlify automatically

**Works on**:
- 💻 Desktop browsers (Chrome, Firefox, Safari, Edge)
- 📱 Mobile devices (iOS, Android)
- 📱 Tablets (iPad, Android tablets)

### **Method 2: Material Library (CLI)**
```bash
python -m src.intelligent_photocopier.main
# Select option 2 → Choose a course (1-6) → Done!
```

### **Method 3: Custom Content (CLI)**
```bash
python -m src.intelligent_photocopier.main
# Select option 1 → Paste your outline → Press Ctrl+D or type 'END'
```

### **Method 4: Quick Start Menu**
```bash
python quickstart.py
# Interactive menu with API testing, demo, and documentation
```

### **Method 5: Pre-configured Demo**
```bash
python src/intelligent_photocopier/demo.py
# Generates a sample course instantly
```

## 🚀 Live Demo — See It in Action

### **Option 1: Use Material Library (Fastest)**
The Intelligent Photocopier includes 6 pre-loaded course outlines in the `material_context/` directory:

```bash
# Run interactive mode
python -m src.intelligent_photocopier.main

# Choose option 2: "Select from material library"
# Available materials:
# 1. A1: Defensive Programming, Errors, and Contracts
# 2. A2: DRY, Cohesion & Coupling, Clean Structure
# 3. B3: Iterators & Generators
# 4. B4: Performance Fundamentals
# 5. B5: Regular Expressions and Text Processing
# 6. C6: Third-Party Libraries and Package Management

# Select any number (e.g., "5") to generate a complete course!
```

**Example: Generate B5 Regular Expressions Course**
```bash
$ python -m src.intelligent_photocopier.main

🤖 Intelligent Photocopier - AI Course Generator
==================================================
✅ OpenAI API configured

📝 Choose input method:
1. 📋 Paste course content directly
2. 📁 Select from material library

Enter your choice (1 or 2): 2

📚 Available Materials:
--------------------------------------------------
1. A1-defensive-programming
2. A2-dry-cohesion-coupling
3. B3-iterators-generators
4. B4-performance-fundamentals
5. B5-regular-expressions
6. C6-third-party-libraries

Select material number: 5

📖 Loading: B5-regular-expressions.md
✅ Loaded 1542 characters

🔍 Analyzing course content...
✨ Generated: B5-regular-expressions-and-text-processing
```

### **Option 2: Paste Your Own Content**
You can also create custom courses by pasting your outline:

**Step 1: Input Course Outline**
```
A2 DRY, Cohesion & Coupling, Clean Structure
Duration: 3-4h

Goal: Refactor for clarity and reuse using DRY while maintaining high cohesion and low coupling.

Topics:
- DRY vs premature abstraction
- Module boundaries and function extraction
- Dependency seams and adapters
```

**Step 2: AI Processing**
The system automatically:
1. 🔍 **Analyzes** your content to extract course information
2. 🧠 **Generates** 7 different content types using AI
3. 📁 **Creates** a complete course directory structure
4. ✅ **Validates** content quality and consistency

**Step 3: Generated Output**
```
Lessons/A2-dry-cohesion-coupling-clean-structure/
├── README.md                    # Professional course overview
├── lesson-content.md           # Complete educational content
├── summary.md                  # Key takeaways and assessment
├── reference/
│   ├── quick_reference.md      # AI-generated quick reference
│   ├── best_practices.md       # Industry best practices
│   └── exercise_instructions.md # Hands-on coding exercises
├── solutions/
│   └── practice_solution.md    # Working code examples
└── tests/
    ├── practice_module.py      # Practice exercises
    └── test_practice.py        # Test cases
```

## 🎓 Course Generation Examples

### **Generated Course: Regular Expressions and Text Processing**
**Input**: B5 course material from library
**Output**: [`Lessons/B5-regular-expressions-and-text-processing/`](Lessons/B5-regular-expressions-and-text-processing/)

**What was generated**:
- ✅ Professional README with course overview and learning objectives
- ✅ Comprehensive lesson content with regex patterns and examples
- ✅ Quick reference guide for common regex operations
- ✅ Best practices for text processing and validation
- ✅ Hands-on exercise instructions with practical examples
- ✅ Practice solutions with Markdown format documentation

## 🌐 Web Interface Features

### **Instant Course Preview** ⚡
No more waiting! See your generated course content immediately:
- 📑 **Multi-file tabs** — Switch between README, lessons, references
- 🎨 **Markdown rendering** — Beautiful formatted preview
- 🚀 **Zero wait time** — Content displays while deployment happens
- 🔄 **Background deployment** — Netlify builds in parallel

### **Mobile-First Design** 📱
Perfect experience on any device:
- 📱 **Responsive breakpoints** — 968px, 640px, 480px optimized
- 👆 **Touch-friendly** — Large buttons, easy navigation
- 📊 **Adaptive layouts** — Grid → Single column on mobile
- 🎯 **Readable typography** — Auto-scaling text sizes

### **Efficient GitHub Integration** 🔧
- 📦 **Batch commits** — All files in single commit (no spam)
- ⚡ **Single Netlify deploy** — One trigger instead of 7
- 📊 **Progress tracking** — Live countdown and progress bar
- ✅ **Auto-deployment** — Push to GitHub → Netlify builds → Live

### **Modern Developer Experience** 🎨
- 🎨 **Gradient UI** — Beautiful purple/blue theme
- ⏱️ **Real-time feedback** — Progress updates every second
- 🔔 **Smart notifications** — Deployment status alerts
- 🌓 **Professional design** — Industry-standard UX patterns

##  Complete Documentation

### **Setup and Usage**
- 📋 [**Setup Guide**](docs/INTELLIGENT_PHOTOCOPIER_GUIDE.md) — Complete installation and configuration
- 📚 [**User Guide**](docs/user-guide.md) — Detailed usage instructions and examples
- 🌐 [**Web Interface Guide**](https://intelligentphotocopier.online/documentation/) — Online documentation
- 🔍 [**Troubleshooting**](docs/troubleshooting.md) — Common issues and solutions

---

## 🧮 Foundation Project: Professional Python Calculator

The Intelligent Photocopier is built on top of a **production-grade Python calculator** that demonstrates industry best practices:

## 🎯 Calculator Features

- **High-performance calculator** with comprehensive test coverage (100%)
- **Production-ready CLI** with professional error handling and validation
- **Complete CI/CD pipeline** with automated testing, security scanning, and deployment
- **Professional codebase** that passes enterprise-grade quality checks
- **VS Code workspace** optimized for Python development
- **Defensive programming skills** through hands-on exercises and real implementations

## 📚 Integrated Course Content

This project includes **comprehensive learning modules** that teach professional software development through practical application:

### 🛡️ **A1: Defensive Programming, Errors, and Contracts**
**Duration**: 3-4 hours | **Level**: Intermediate

Learn to write resilient code that fails fast, communicates intent, and recovers gracefully:

- ✅ **EAFP vs LBYL** — Choose the right approach with clear justification
- ✅ **Custom Exception Hierarchies** — Design meaningful error handling systems
- ✅ **Design by Contract** — Implement preconditions, postconditions, and invariants
- ✅ **Guard Clauses** — Simplify complex conditional logic
- ✅ **Secure Logging** — Handle sensitive data safely in error messages
- ✅ **Error Path Testing** — Comprehensive testing strategies for edge cases

**Hands-on Components:**
- 🧮 **Calculator Module** — Practice defensive programming with mathematical operations
- ⚙️ **Configuration Loader** — Harden file loading and parsing logic
- 🧪 **Complete Test Suite** — Learn to test error scenarios effectively
- 📋 **Reference Implementations** — Study production-ready defensive patterns

**Location**: [`Lessons/A1-Defensive-Programming/`](Lessons/A1-Defensive-Programming/)

**🚀 Quick Start**: Review the [lesson content](Lessons/A1-Defensive-Programming/lesson-content.md) and explore the [practice exercises](Lessons/A1-Defensive-Programming/reference/exercise_instructions.md)!

### 🔮 **Intelligent Photocopier: AI Course Generator**
**NEW**: AI-powered course creation system that generates new programming courses using the A1 template as a foundation.

**Features:**
- 🤖 **OpenAI GPT-4o-mini Integration** — Intelligent content generation
- 📚 **Material Library** — 6 pre-loaded course outlines ready to generate (A1-A2, B3-B5, C6)
- 🔄 **Dual Input Modes** — Select from material library or paste custom content
- 📋 **Template-Based Structure** — Uses A1-Defensive-Programming as a blueprint
- 🎯 **Context-Aware Content** — Generates relevant exercises and examples
- 📁 **Complete Course Creation** — README, lessons, tests, and reference materials
- ⚡ **Quick Start Scripts** — Easy setup and testing

**Material Library Courses:**
```
material_context/
├── A1-defensive-programming.md     # Errors, exceptions, contracts
├── A2-dry-cohesion-coupling.md     # Code structure and refactoring
├── B3-iterators-generators.md      # Python iterators and generators
├── B4-performance-fundamentals.md  # Performance optimization
├── B5-regular-expressions.md       # Text processing and regex
└── C6-third-party-libraries.md     # Package management
```

**Quick Start:**
```bash
# 1. Set up OpenAI API key
cp .env.example .env
# Edit .env and add your OpenAI API key

# 2. Run the quick start script
python quickstart.py

# 3. Or use interactive mode with material library
python -m src.intelligent_photocopier.main
# Choose option 2: "Select from material library"
# Pick any course (1-6) and generate instantly!
```

**Location**: [`src/intelligent_photocopier/`](src/intelligent_photocopier/)

### 🔮 **Coming Soon: Additional Modules**
- **B1: Code Quality & Static Analysis** — Automated quality enforcement
- **C1: Performance Optimization** — Profiling and optimization techniques
- **D1: Security Best Practices** — Building secure Python applications

## 🚀 Platform Setup — Start Here First!

**All commands in this project use Unix/Linux standards.** Choose your platform:

### 🍎 **macOS Users — You're Ready!**
Your terminal already supports all commands. Proceed to [Quick Start](#quick-start).

### 🪟 **Windows Users — Enable Unix/Linux Environment**

**Option 1: WSL2 Ubuntu (Recommended)**
```powershell
# Run in PowerShell as Administrator
wsl --install -d Ubuntu
# Restart your computer when prompted
# After restart, complete Ubuntu setup with username/password
```

**Option 2: Git Bash**
- Install [Git for Windows](https://git-scm.windows.com/) with Git Bash
- Use Git Bash terminal for all commands

### 🐧 **Linux Users — You're Ready!**
Your terminal already supports all commands. Proceed to [Quick Start](#quick-start).

---

## ⚡ Quick Start (2 minutes)

**Prerequisites**: Python 3.11+ and Git installed

```bash
# 1. Clone and enter the project
git clone https://github.com/chengxin199/IS601_MidtermProject_Intelligent-Photocopier.git
cd code_quality_calc

# 2. Set up Python environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows Git Bash: source .venv/Scripts/activate
python -m pip install --upgrade pip

# 3. Install development tools
pip install -r requirements-dev.txt

# 4. Verify everything works
pytest --cov=src --cov-report=term-missing -q
```

**✅ Success!** You should see all tests passing with 93%+ coverage.

## 🎮 Try It Out

**Basic calculator operations:**
```bash
# Method 1: Direct module execution
python -m src.main add 2 3        # Output: 5.0
python -m src.main multiply 4 5   # Output: 20.0
python -m src.main divide 10 2    # Output: 5.0

# Method 2: Install as CLI tool
pip install -e .
calc add 2 3                      # Output: 5.0
calc subtract 10 3                # Output: 7.0
```

**Explore defensive programming lessons:**
```bash
# Navigate to the course content
cd Lessons/A1-Defensive-Programming/

# Try the practice modules (intentionally vulnerable)
python tests/calculator.py

# Study the hardened implementations
python tests/test_calculator_hardened.py

# Run comprehensive tests
pytest tests/test_calculator_hardened.py -v
```

**Run the complete quality suite:**
```bash
# Option 1: Individual commands
pytest --cov=src --cov-report=term-missing -q
flake8 $(git ls-files '*.py' | tr '\n' ' ')
pylint -j 0 $(git ls-files '*.py' | tr '\n' ' ')
mypy src
make security

# Option 2: VS Code task (if using VS Code)
# Command Palette → "Run Task" → "quality: all"

# Option 3: Makefile shortcut
make qa
```

## 🎓 Learning Path

This project includes a **comprehensive learning system** with multiple tracks designed for professional development:

### 📚 **Documentation**
- 📋 [**Setup Guide**](docs/INTELLIGENT_PHOTOCOPIER_GUIDE.md) — Get started quickly
- 📚 [**User Guide**](docs/user-guide.md) — Complete usage instructions
- 🔍 [**Troubleshooting**](docs/troubleshooting.md) — Solve common issues

### 🛡️ **Defensive Programming Course**
**Master professional coding practices:** [`Lessons/A1-Defensive-Programming/`](Lessons/A1-Defensive-Programming/)

**Complete hands-on curriculum:**
- 📖 [Lesson Content](Lessons/A1-Defensive-Programming/lesson-content.md) — Theory and concepts
- 💻 [Practice Exercises](Lessons/A1-Defensive-Programming/tests/) — Real coding challenges
- ✅ [Reference Solutions](Lessons/A1-Defensive-Programming/tests/test_calculator_hardened.py) — Production-ready implementations
- 📋 [Exercise Instructions](Lessons/A1-Defensive-Programming/reference/exercise_instructions.md) — Step-by-step guidance
- 🎯 [Summary & Assessment](Lessons/A1-Defensive-Programming/summary.md) — Learning validation

**What makes this special:**
- **Real Implementation** — Not just theory, but working code you can run and test
- **Industry Patterns** — Learn the same defensive programming techniques used at top tech companies
- **Security Focus** — Understand how to handle sensitive data safely
- **Complete Testing** — Master error path testing and edge case validation

### 🏗️ **Project Structure**
```
code_quality_calc/
├── src/                          # Calculator implementation
│   ├── main.py                   # CLI entry point
│   └── operations/               # Mathematical operations
├── tests/                        # 100% test coverage
├── .vscode/                      # VS Code configuration
├── .github/workflows/            # CI/CD automation
├── docs/                         # Complete learning guide
├── Lessons/                      # Course content and exercises
│   └── A1-Defensive-Programming/ # Defensive programming lesson
└── pyproject.toml               # Modern Python packaging
```

### 🛠️ **Professional Tools Integrated**
- **Testing**: pytest with coverage reporting
- **Code Quality**: Black, isort, Flake8, Pylint
- **Type Safety**: mypy static type checking
- **Security**: Bandit, pip-audit, Dependabot
- **CI/CD**: GitHub Actions with automated quality gates
- **IDE**: VS Code with optimized Python development setup

## 🎓 What You'll Learn

### **Foundation Skills**
- ✅ Professional Python project structure (`src/` layout)
- ✅ Virtual environment management and dependency isolation
- ✅ Test-driven development with 100% coverage
- ✅ Code formatting and quality standards (PEP 8)
- ✅ Static type checking for reliability

### **Defensive Programming Mastery**
- ✅ **EAFP vs LBYL** — Choose the right error handling approach
- ✅ **Custom Exception Design** — Build meaningful error hierarchies
- ✅ **Input Validation** — Secure and robust data handling
- ✅ **Contract Programming** — Implement preconditions and postconditions
- ✅ **Guard Clauses** — Write clean, readable error handling code
- ✅ **Secure Logging** — Protect sensitive data in error messages
- ✅ **Error Path Testing** — Comprehensive edge case validation

### **Professional Practices**
- ✅ Continuous Integration and automated testing
- ✅ Security scanning and vulnerability management
- ✅ Professional Git workflows and commit practices
- ✅ Command-line interface design and packaging
- ✅ Performance monitoring and optimization

### **Industry Tools**
- ✅ VS Code configuration for Python development
- ✅ GitHub Actions for CI/CD pipelines
- ✅ Docker containerization (advanced topics)
- ✅ Documentation and project maintenance
- ✅ Collaboration and code review processes

## 🏗️ Technical Architecture

### **Deployment Stack**
```
User Browser (Mobile/Desktop)
    ↓
Netlify CDN (intelligentphotocopier.online)
    ↓ Static Site (Eleventy)
    ↓
Render.com API (intelligent-photocopier.onrender.com)
    ↓ Flask REST API
    ↓
OpenAI GPT-4o-mini API
    ↓
GitHub Repository (Auto-commit)
    ↓
Netlify Auto-Deploy (Webhook trigger)
```

### **Technology Components**
- **Frontend**: Eleventy (11ty) static site generator, Nunjucks templates
- **Backend API**: Flask REST API hosted on Render.com
- **AI Engine**: OpenAI GPT-4o-mini for content generation
- **Storage**: GitHub repository as content database
- **CDN**: Netlify for global edge distribution
- **Domain**: intelligentphotocopier.online (via Netlify DNS)

### **Key Features Implementation**
- **Instant Preview**: sessionStorage + marked.js for client-side Markdown rendering
- **Batch Commits**: GitHub Tree API for atomic multi-file commits
- **Responsive Design**: CSS Grid with mobile-first breakpoints (968px, 640px, 480px)
- **Deployment Tracking**: JavaScript countdown with progress bar animation
- **Auto-Deploy**: GitHub → Netlify webhook integration

## 🆘 Need Help?

### **Quick Troubleshooting**
```bash
# Common issues and solutions

# Issue: ModuleNotFoundError
# Solution: Activate virtual environment and run from project root
source .venv/bin/activate
cd /path/to/code_quality_calc

# Issue: Import errors in VS Code
# Solution: Select correct Python interpreter
# VS Code → Bottom status bar → Select .venv/bin/python

# Issue: Tests failing
# Solution: Ensure all dependencies installed
pip install -r requirements-dev.txt
pytest --cov=src --cov-report=term-missing
```

### **Comprehensive Support**
- 📖 **User Guide**: [`docs/user-guide.md`](docs/user-guide.md)
- 🔧 **Setup Instructions**: [`docs/INTELLIGENT_PHOTOCOPIER_GUIDE.md`](docs/INTELLIGENT_PHOTOCOPIER_GUIDE.md)
- 🔍 **Troubleshooting**: [`docs/troubleshooting.md`](docs/troubleshooting.md)

## 🌟 Why This Approach Works

### **Real-World Relevance**
Every tool and practice in this project is used daily by professional Python developers. You're not just learning syntax—you're mastering the **complete professional workflow**.

### **Portfolio Ready**
This project demonstrates professional competency to employers:
- Clean, tested, documented code
- Modern development practices
- CI/CD pipeline experience
- Production-ready software design

### **Foundation for Growth**
The patterns you learn here scale from simple calculators to complex distributed systems. These are the **fundamentals that matter** for any Python career path.

---

## 📈 Next Steps

1. **Start Learning**: Review the [**Setup Guide**](docs/INTELLIGENT_PHOTOCOPIER_GUIDE.md) to get started
2. **Master Defensive Programming**: Explore [A1 Lesson Content](Lessons/A1-Defensive-Programming/lesson-content.md) 🛡️
3. **Generate Static Website**: Create a beautiful course website with [Eleventy](docs/eleventy-integration.md) 🌐
4. **Try Exercises**: Each lesson includes hands-on activities
5. **Build Your Version**: Fork this repo and customize it
6. **Generate Courses**: Use the AI-powered course generator

### 🌐 Static Website Generation

The Intelligent Photocopier now supports generating beautiful static websites from your courses using Eleventy!

**Quick Start:**
```bash
# Generate courses as usual
python -m src.intelligent_photocopier.main

# Install Node.js dependencies
npm install

# Build and serve website
npm run serve
# Visit http://localhost:8080
```

**Features:**
- ✨ Professional, responsive design
- 🎨 Syntax highlighting for code
- 📱 Mobile-friendly layouts
- 🚀 Deploy to GitHub Pages, Netlify, Vercel
- 🔍 SEO-friendly static HTML

**Learn More:** [Eleventy Integration Guide](docs/eleventy-integration.md)

---

**Ready to build professional-grade Python software?** [Start your journey here →](docs/INTELLIGENT_PHOTOCOPIER_GUIDE.md)
