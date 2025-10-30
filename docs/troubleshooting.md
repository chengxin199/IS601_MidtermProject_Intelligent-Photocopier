# Troubleshooting Guide

## Common Issues and Solutions

### Installation Issues

#### "No module named 'openai'"
**Problem**: Dependencies not installed
```bash
# Solution
pip install -r requirements-dev.txt
```

#### "Python version not supported"
**Problem**: Python version too old
```bash
# Check version
python --version

# Solution: Install Python 3.11+
# On Ubuntu/Debian:
sudo apt update
sudo apt install python3.11

# On macOS with Homebrew:
brew install python@3.11
```

### API Configuration Issues

#### "No OpenAI API key found"
**Problem**: Environment not configured
```bash
# Solution 1: Create .env file
echo "OPENAI_API_KEY=your_key_here" > .env

# Solution 2: Set environment variable
export OPENAI_API_KEY=your_key_here
```

#### "API key invalid"
**Problem**: Wrong or expired API key
```bash
# Test your key
python src/intelligent_photocopier/test_api.py

# Solution: Get new key from https://platform.openai.com/api-keys
```

#### "Rate limit exceeded"
**Problem**: Too many API calls
**Solution**: Wait a few minutes and try again, or upgrade your OpenAI plan

### Course Generation Issues

#### "Template not found"
**Problem**: A1-Defensive-Programming directory missing
```bash
# Check if template exists
ls -la Lessons/A1-Defensive-Programming/

# Solution: Ensure the template course is present
```

#### "Permission denied" when creating files
**Problem**: Insufficient file system permissions
```bash
# Solution
chmod 755 Lessons/
mkdir -p Lessons/test && rm -rf Lessons/test
```

#### "Empty course generated"
**Problem**: AI generation failed, fell back to placeholders
**Solutions**:
1. Check API key configuration
2. Verify internet connection
3. Try again (temporary API issues)
4. Use placeholder content as starting point

### Content Quality Issues

#### "Generated content is repetitive"
**Problem**: AI model limitations or prompt issues
**Solutions**:
1. Provide more detailed course descriptions
2. Include specific learning objectives
3. Add context about target audience
4. Try generating again for variation

#### "Course title not extracted correctly"
**Problem**: Input format not recognized
**Supported formats**:
```
# Format 1: Standard markdown
# A2: Course Title

# Format 2: Simple format
A2 Course Title [Level]

# Format 3: Course prefix
Course: Title Name

# Format 4: Plain title
Course Title Here
```

### System Performance Issues

#### "Course generation takes too long"
**Normal time**: 30-60 seconds per course
**Solutions**:
1. Check internet connection
2. Verify API service status
3. Try with shorter course descriptions

#### "Out of memory errors"
**Problem**: Large content processing
**Solutions**:
1. Close other applications
2. Process one course at a time
3. Restart the application

### Development Issues

#### "Tests failing"
**Problem**: Environment setup or code changes
```bash
# Run specific test
pytest tests/test_operations.py -v

# Run all tests with details
pytest tests/ -v --tb=short

# Check test coverage
pytest --cov=src tests/
```

#### "Type checking errors"
**Problem**: Type annotation issues
```bash
# Run type checker
mypy src/

# Common fixes:
# - Add type annotations
# - Import proper types
# - Use Optional for nullable values
```

#### "Linting errors"
**Problem**: Code style issues
```bash
# Check code style
flake8 src/

# Auto-fix formatting
black src/
isort src/
```

## Debugging Steps

### 1. Enable Debug Logging
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### 2. Test Individual Components
```bash
# Test content analyzer
python -c "
from src.intelligent_photocopier.content_analyzer import ContentAnalyzer
analyzer = ContentAnalyzer()
result = analyzer.analyze_content('A2: Test Course')
print(result)
"

# Test AI generation
python src/intelligent_photocopier/test_api.py

# Test file operations
python -c "
from src.intelligent_photocopier.file_manager import FileManager
fm = FileManager()
print('FileManager initialized successfully')
"
```

### 3. Verify Environment
```bash
# Check Python version
python --version

# Check installed packages
pip list | grep -E "(openai|pytest|mypy)"

# Check environment variables
echo $OPENAI_API_KEY

# Test basic functionality
python quickstart.py
```

## Error Message Reference

### Common Error Messages

**"ModuleNotFoundError: No module named 'src'"**
```bash
# Solution: Run from project root directory
cd /path/to/code_quality_calc
python quickstart.py
```

**"FileNotFoundError: [Errno 2] No such file or directory: '.env'"**
```bash
# Solution: Create .env file or set environment variables
cp .env.example .env
# Edit .env with your settings
```

**"openai.AuthenticationError: Incorrect API key"**
```bash
# Solution: Check API key format and validity
# API keys start with 'sk-' and are 48+ characters long
```

**"TypeError: 'NoneType' object is not iterable"**
- Usually indicates missing API response
- Check internet connection and API status
- Verify API key configuration

## Getting Help

### 1. Check Documentation
- [User Guide](user-guide.md) - Usage instructions
- [Technical Architecture](technical-architecture.md) - System details
- [Implementation Journey](implementation-journey.md) - Development insights

### 2. Review Examples
- Generated courses in `Lessons/` directory
- Test files in `tests/` directory
- Demo script: `src/intelligent_photocopier/demo.py`

### 3. Debug Information to Collect
When reporting issues, include:
```bash
# System information
python --version
pip list

# Error details
# Copy the full error message and stack trace

# Environment
cat .env  # (remove sensitive data)
ls -la Lessons/

# Test results
python src/intelligent_photocopier/test_api.py
```

### 4. Minimal Reproduction
Create a minimal example that reproduces the issue:
```python
from src.intelligent_photocopier.content_analyzer import ContentAnalyzer

analyzer = ContentAnalyzer()
result = analyzer.analyze_content("A2: Test Course")
print(result)
```

## Prevention Tips

### Regular Maintenance
```bash
# Update dependencies periodically
pip install --upgrade -r requirements-dev.txt

# Run full test suite
pytest tests/ -v

# Check code quality
flake8 src/
mypy src/
```

### Environment Best Practices
1. Use virtual environments
2. Keep dependencies updated
3. Back up your .env file
4. Version control your courses
5. Test after system updates

### API Usage Best Practices
1. Monitor API usage and limits
2. Implement proper error handling
3. Use appropriate models for your needs
4. Cache results when appropriate
5. Have fallback plans for API outages
