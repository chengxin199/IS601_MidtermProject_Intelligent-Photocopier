---
layout: layouts/base.njk
title: Home
permalink: /index.html
---

<h1>🤖 Welcome to Intelligent Photocopier</h1>

<p style="font-size: 1.2rem; color: #555; margin-bottom: 2rem;">
  AI-powered course generation tool that creates professional programming courses from your content.
</p>

<div style="background: linear-gradient(135deg, #667eea22 0%, #764ba222 100%); padding: 2rem; border-radius: 8px; margin-bottom: 3rem;">
  <h2 style="border: none;">✨ Features</h2>
  <ul style="margin-left: 0; list-style: none;">
    <li style="margin-bottom: 1rem;">📚 <strong>Material Library:</strong> Pre-loaded professional courses ready to use</li>
    <li style="margin-bottom: 1rem;">🎨 <strong>Custom Content:</strong> Generate courses from your own materials</li>
    <li style="margin-bottom: 1rem;">🤖 <strong>AI-Powered:</strong> Leverages OpenAI GPT-4o-mini for intelligent content generation</li>
    <li style="margin-bottom: 1rem;">📖 <strong>Complete Structure:</strong> README, lessons, summaries, references, and solutions</li>
    <li style="margin-bottom: 1rem;">🌐 <strong>Static Websites:</strong> Beautiful course websites with Eleventy</li>
  </ul>
</div>

<h2>📚 Available Courses</h2>

{% set courseList = collections.courses %}
{% if courseList.length > 0 %}
<div class="course-grid">
{% for course in courseList %}
  <div class="course-card">
    <h3><a href="{{ course.url }}">{{ course.data.title }}</a></h3>
    <p>{{ course.data.description or 'Explore this course...' }}</p>
    <div style="margin-top: 1rem;">
      {% if course.data.level %}
      <span style="background: #667eea; color: white; padding: 0.25rem 0.75rem; border-radius: 3px; font-size: 0.85rem; margin-right: 0.5rem;">{{ course.data.level }}</span>
      {% endif %}
      {% if course.data.courseId %}
      <span style="background: #e0e0e0; color: #333; padding: 0.25rem 0.75rem; border-radius: 3px; font-size: 0.85rem;">{{ course.data.courseId }}</span>
      {% endif %}
    </div>
    <a href="{{ course.url }}" class="btn" style="margin-top: 1.5rem;">View Course →</a>
  </div>
{% endfor %}
</div>
{% else %}
<div style="text-align: center; padding: 3rem; background: #f8f9fa; border-radius: 8px;">
  <p style="font-size: 1.2rem; color: #666;">No courses generated yet. Run the Intelligent Photocopier to create your first course!</p>
  <a href="https://github.com/chengxin199/IS601_MidtermProject_Intelligent-Photocopier" class="btn" style="margin-top: 1rem;">Get Started on GitHub →</a>
</div>
{% endif %}

<div style="margin-top: 3rem; padding: 2rem; background: #fff3cd; border-left: 4px solid #ffc107; border-radius: 8px;">
  <h3>🚀 Quick Start</h3>
  <pre><code class="language-bash"># Clone the repository
git clone https://github.com/chengxin199/IS601_MidtermProject_Intelligent-Photocopier.git
cd IS601_MidtermProject_Intelligent-Photocopier

# Set up environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Configure OpenAI API
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# Run the tool
python -m src.intelligent_photocopier.main

# Generate static website
npm install
npm run build
npm run serve  # View at http://localhost:8080
</code></pre>
</div>
