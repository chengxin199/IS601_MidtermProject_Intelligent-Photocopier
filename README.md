![CI](https://github.com/kaw393939/code_quality_calc/actions/workflows/quality.yml/badge.svg?branch=main)

# 🧮 Professional Python Calculator — Learn Industry-Grade Development .

> **Transform a simple calculator into production-ready software** while mastering professional Python development practices used by top tech companies.

This isn't just another coding tutorial. You'll build a **real production system** with the same tools, processes, and quality standards used at companies like Google, Netflix, and Spotify.

## 🎯 What You'll Build

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

**🚀 Quick Start**: Follow the complete [**Defensive Programming Learning Guide**](DEFENSIVE_PROGRAMMING_GUIDE.md) for step-by-step instructions!

### 🔮 **Intelligent Photocopier: AI Course Generator**
**NEW**: AI-powered course creation system that generates new programming courses using the A1 template as a foundation.

**Features:**
- 🤖 **OpenAI GPT-4 Integration** — Intelligent content generation
- 📋 **Template-Based Structure** — Uses A1-Defensive-Programming as a blueprint
- 🎯 **Context-Aware Content** — Generates relevant exercises and examples
- 📁 **Complete Course Creation** — README, lessons, tests, and reference materials
- ⚡ **Quick Start Scripts** — Easy setup and testing

**Quick Start:**
```bash
# 1. Set up OpenAI API key
cp .env.example .env
# Edit .env and add your OpenAI API key

# 2. Run the quick start script
python quickstart.py

# 3. Or use interactive mode
python -m src.intelligent_photocopier.main
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

**✅ Success!** You should see all tests passing with 100% coverage.

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

## 🎯 Learning Path

This project includes a **comprehensive learning system** with multiple tracks designed for professional development:

### 📚 **Core Development Guide**
**Start here:** [`docs/index.md`](docs/index.md) — Complete textbook with 15+ chapters

**Quick navigation:**
- 🚀 [Project Overview](docs/01-overview.md) — Understanding the goals
- ⚙️ [Setup Guide](docs/02-setup.md) — Detailed environment setup
- 🧪 [Testing](docs/05-testing.md) — Achieving 100% test coverage
- 💻 [VS Code Setup](docs/09-vscode.md) — Professional IDE configuration
- 🔄 [CI/CD](docs/08-ci.md) — Automated quality checks

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
- 📖 **Detailed troubleshooting**: [`docs/12-troubleshooting.md`](docs/12-troubleshooting.md)
- 🔧 **Configuration guide**: [`docs/appendix-configs.md`](docs/appendix-configs.md)
- 💼 **Career guidance**: [`docs/careers.md`](docs/careers.md)
- 📝 **Glossary**: [`docs/glossary.md`](docs/glossary.md)

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

1. **Start Learning**: Open [`docs/index.md`](docs/index.md) for the complete guide
2. **Master Defensive Programming**: Follow the [**Defensive Programming Learning Guide**](DEFENSIVE_PROGRAMMING_GUIDE.md) 🛡️
3. **Try Exercises**: Each chapter includes hands-on activities
4. **Build Your Version**: Fork this repo and customize it
5. **Join the Community**: Share your progress and get help

**Ready to build professional-grade Python software?** [Start your journey here →](docs/index.md)
