#!/bin/bash
# Start the AI Course Builder API server

echo "🚀 Starting AI Course Builder API..."
echo ""

# Check if virtual environment is activated
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate
fi

# Check if Flask is installed
if ! python -c "import flask" 2>/dev/null; then
    echo "Installing API dependencies..."
    pip install flask flask-cors openai
    echo ""
fi

echo "Starting Flask API server on http://localhost:5000"
echo "Press Ctrl+C to stop"
echo ""

# Start the server
python -m src.intelligent_photocopier.api
