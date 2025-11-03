# 🤖 Intelligent Photocopier - Complete Setup Guide

Welcome to the **Intelligent Photocopier**, an AI-powered course generator that creates comprehensive programming courses using your A1-Defensive-Programming lesson as a template.

## 🚀 Quick Setup (5 minutes)

### Step 1: Get Your OpenAI API Key

1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign in or create an account
3. Navigate to "API Keys" section
4. Click "Create new secret key"
5. Copy your API key (starts with `sk-...`)

### Step 2: Configure the System

```bash
# 1. Navigate to your project directory
cd /path/to/code_quality_calc

# 2. Create configuration file
cp .env.example .env

# 3. Edit the .env file and add your API key
# Replace 'your_openai_api_key_here' with your actual key
nano .env   # or use any text editor
```

Your `.env` file should look like:
```properties
OPENAI_API_KEY=sk-your-actual-api-key-here
OPENAI_MODEL=gpt-4o-mini
MAX_TOKENS=2000
TEMPERATURE=0.7
```

### Step 3: Test the Setup

```bash
# Run the quick start script
python quickstart.py

# Or test directly
python src/intelligent_photocopier/test_api.py
```

## 🎯 Usage Methods

### Method 1: Quick Start Script (Recommended)
```bash
python quickstart.py
```
**Features:**
- Interactive menu system
- Automatic setup checking
- API connection testing
- Multiple demo options

### Method 2: Direct Demo
```bash
python src/intelligent_photocopier/demo.py
```
**Features:**
- Generates sample B2-Performance-Optimization course
- Shows complete workflow
- Works with or without API key

### Method 3: Interactive Mode
```bash
python -m src.intelligent_photocopier.main
```
**Features:**
- Custom course input
- Paste your own course content
- Full AI content generation

### Method 4: API Testing Only
```bash
python src/intelligent_photocopier/test_api.py
```
**Features:**
- Tests API connection
- Validates configuration
- Quick content generation test

## 📋 What Each Mode Does

### 🧪 **API Test Mode**
- Tests OpenAI API connection
- Validates configuration
- Generates sample content snippet
- **Best for:** Verifying setup

### 🎭 **Demo Mode**
- Generates complete B2-Performance-Optimization course
- Uses predefined course content
- Creates all course files (README, lessons, tests, etc.)
- **Best for:** Seeing the full system in action

### 🚀 **Interactive Mode**
- Prompts you to input your own course content
- Analyzes your input to extract course information
- Generates custom course based on your content
- **Best for:** Creating your own courses

### 📖 **Documentation Mode**
- Shows helpful links and guides
- Explains configuration options
- Provides troubleshooting tips
- **Best for:** Learning about the system

## 📁 Generated Course Structure

When you generate a course, you'll get a complete directory structure:

```
Lessons/[CourseID]/
├── README.md              # Course overview and objectives
├── lesson-content.md      # Detailed lesson content
├── summary.md            # Course summary and key takeaways
├── reference/
│   ├── additional_reading.md
│   ├── exercise_instructions.md
│   └── best_practices.md
├── solutions/
│   └── [generated solution files]
└── tests/
    └── [generated test files]
```

## 🔧 Configuration Options

### Environment Variables (.env file)

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | *required* | Your OpenAI API key |
| `OPENAI_MODEL` | `gpt-4o-mini` | AI model to use |
| `MAX_TOKENS` | `2000` | Maximum tokens per API call |
| `TEMPERATURE` | `0.7` | AI creativity level (0.0-1.0) |

### Model Options
- **gpt-4o-mini** (recommended): Fast, cost-effective, good quality
- **gpt-4o**: Higher quality, more expensive
- **gpt-3.5-turbo**: Fastest, lowest cost, basic quality

## 🎓 Example Course Input

When using interactive mode, provide course content like this:

```markdown
# C1: Security Best Practices in Python

Learn to build secure Python applications that protect against common vulnerabilities and follow industry security standards.

This comprehensive course covers secure coding practices, authentication, authorization, data protection, and security testing methodologies used in enterprise environments.

## Learning Objectives
- Implement secure authentication and authorization systems
- Protect against common vulnerabilities (OWASP Top 10)
- Handle sensitive data securely
- Implement security logging and monitoring
- Perform security testing and code analysis

## Topics Covered
- Input validation and sanitization
- Authentication and session management
- Encryption and data protection
- SQL injection prevention
- Cross-site scripting (XSS) prevention
- Security testing and static analysis

Duration: 5-6 hours
Level: Advanced
Prerequisites:
- Strong Python programming skills
- Understanding of web development concepts
- Basic knowledge of networking and databases
```

## 🚨 Troubleshooting

### ❌ "Invalid API Key" Error
**Problem:** API key is incorrect or not set
**Solution:**
1. Check your `.env` file has the correct API key
2. Ensure no extra spaces or quotes around the key
3. Verify the key is active at [OpenAI Platform](https://platform.openai.com/api-keys)

### ❌ "ModuleNotFoundError"
**Problem:** Python modules not found
**Solution:**
```bash
# Ensure virtual environment is activated
source .venv/bin/activate

# Install requirements
pip install -r requirements-dev.txt

# Run from project root directory
cd /path/to/code_quality_calc
```

### ❌ "Rate Limit Exceeded"
**Problem:** Too many API calls
**Solution:**
- Wait a few minutes and try again
- Consider upgrading your OpenAI plan
- Use a lower `TEMPERATURE` value for more consistent results

### ❌ "Template Source Not Found"
**Problem:** A1-Defensive-Programming directory missing
**Solution:**
- Ensure you're in the correct project directory
- The `Lessons/A1-Defensive-Programming/` directory must exist
- This serves as the template for new courses

## 🎉 Success Indicators

You'll know everything is working when you see:
- ✅ Configuration validation passes
- ✅ API connection test succeeds
- ✅ Course files are generated in `Lessons/[CourseID]/`
- ✅ No error messages in the output

## 💡 Tips for Best Results

1. **Provide detailed course descriptions** for better AI content generation
2. **Include specific learning objectives** to get targeted course content
3. **Specify prerequisites and duration** for accurate course scoping
4. **Use clear topic lists** to ensure comprehensive coverage
5. **Test with demo mode first** to understand the output format

## 🔗 Additional Resources

- **OpenAI API Documentation**: https://platform.openai.com/docs
- **Project Repository**: https://github.com/chengxin199/IS601_MidtermProject_Intelligent-Photocopier
- **VS Code Setup Guide**: `docs/09-vscode.md`
- **Defensive Programming Course**: `Lessons/A1-Defensive-Programming/`

---

**Ready to generate your first AI-powered course?** Start with: `python quickstart.py` 🚀
