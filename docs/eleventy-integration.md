# 🌐 Static Website Generation with Eleventy

The Intelligent Photocopier now supports generating beautiful static websites from your course content using [Eleventy](https://www.11ty.dev/) (11ty).

## Features

- **Automatic Front Matter**: All generated markdown files include YAML front matter for Eleventy
- **Professional Templates**: Pre-built Nunjucks templates with responsive design
- **Mobile-First Design**: Optimized for all screen sizes with 3 breakpoints (968px, 640px, 480px)
- **Course Collections**: Automatic course listing and navigation
- **Syntax Highlighting**: Code blocks with Prism.js highlighting
- **Fast & Static**: No server needed, deploy anywhere (GitHub Pages, Netlify, Vercel)

## Quick Start

### 1. Install Node.js Dependencies

```bash
npm install
```

This installs:
- Eleventy (static site generator)
- Eleventy Syntax Highlighting plugin
- Markdown-it and markdown-it-anchor

### 2. Generate Courses

Use the Intelligent Photocopier to create courses as usual:

```bash
python -m src.intelligent_photocopier.main
```

All generated markdown files will automatically include Eleventy front matter.

### 3. Build the Website

```bash
# Build static site
npm run build

# Or use the Python helper script
python generate_site.py build
```

The static website will be generated in the `_site/` directory.

### 4. Preview Locally

```bash
# Start development server
npm run serve

# Or use the Python helper script
python generate_site.py serve
```

Visit http://localhost:8080 to view your course website.

## Website Structure

```
_site/                    # Generated static website
├── index.html           # Homepage with course list
├── [course-name]/       # Individual course pages
│   ├── index.html       # Course README
│   ├── lesson-content.html
│   ├── summary.html
│   ├── reference/
│   └── solutions/
└── css/                 # Styles (from templates)
```

## Configuration Files

### `.eleventy.js`
Main Eleventy configuration:
- Input directory: `Lessons/`
- Output directory: `_site/`
- Template engine: Nunjucks
- Markdown processing with anchors
- Syntax highlighting enabled

### `package.json`
NPM scripts:
- `build` - Build static site
- `serve` - Start dev server with hot reload
- `clean` - Remove `_site/` directory

### `_includes/`
Template files:
- `layouts/base.njk` - Base HTML layout with header, nav, footer
- `layouts/course.njk` - Course-specific layout with metadata
- Components for reusable elements

## Python Helper Script

The `generate_site.py` script provides convenient commands:

```bash
# Install dependencies
python generate_site.py install

# Build website
python generate_site.py build

# Start dev server
python generate_site.py serve

# Clean output directory
python generate_site.py clean

# Default (build + serve)
python generate_site.py
```

## Front Matter Structure

Each generated markdown file includes YAML front matter:

```yaml
---
title: Course Title
layout: layouts/course.njk
courseId: A1
level: Intermediate
duration: 2-3 hours
description: Course description
tags:
  - course
  - programming
  - intermediate
date: 2025-01-23T12:34:56
---
```

This metadata is used by Eleventy for:
- Page titles and SEO
- Layout selection
- Course collections and filtering
- Navigation and breadcrumbs

## Customization

### Responsive Design

The templates use mobile-first responsive design with breakpoints:
- **≤480px**: Mobile phones (single column, collapsed navigation)
- **≤640px**: Small tablets (adjusted spacing and fonts)
- **≤968px**: Tablets and small desktops (sidebar moves to top)
- **>968px**: Desktop (full layout with sidebar)

Key responsive features:
- Collapsible navigation on mobile
- Flexible course grid (1-3 columns based on screen size)
- Responsive typography (rem units with viewport scaling)
- Touch-friendly buttons and links
- Optimized images and media queries

### Modify Styles

Edit the CSS in `_includes/layouts/base.njk`:
- Colors: Change gradient colors and accent colors
- Typography: Modify font families and sizes
- Layout: Adjust container widths and spacing

### Add Custom Pages

Create markdown or Nunjucks files in the root or `Lessons/` directory with front matter:

```yaml
---
layout: layouts/base.njk
title: About
permalink: /about/
---

# About This Course Platform
...
```

### Change Templates

Edit `_includes/layouts/*.njk` files to modify:
- HTML structure
- Navigation elements
- Footer content
- Metadata display

## Deployment

### GitHub Pages

```bash
# Build site
npm run build

# Deploy _site/ directory to gh-pages branch
# Or configure GitHub Actions to build automatically
```

### Netlify

1. Connect your repository to Netlify
2. Set build command: `npm install && npm run build`
3. Set publish directory: `_site`
4. Deploy automatically on git push

### Vercel

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel
```

Or connect repository through Vercel dashboard.

## Troubleshooting

### Node.js Not Found

Install Node.js from https://nodejs.org/ (LTS version recommended).

### Eleventy Not Found

```bash
npm install
```

### Build Fails

Check that:
- All markdown files have valid YAML front matter
- No syntax errors in Nunjucks templates
- `Lessons/` directory exists with course content

### No Courses Showing

- Ensure courses have been generated in `Lessons/` directory
- Each course should have a `README.md` with front matter
- Rebuild the site: `npm run build`

## Development Workflow

1. **Generate Course**: `python -m src.intelligent_photocopier.main`
2. **Start Dev Server**: `npm run serve`
3. **Edit Templates**: Changes auto-reload in browser
4. **Build for Production**: `npm run build`
5. **Deploy**: Push `_site/` to hosting provider

## Technical Details

### Why Eleventy?

- **Fast**: No client-side JavaScript framework overhead
- **Flexible**: Use any template language (Nunjucks, Liquid, etc.)
- **Simple**: Markdown-first with easy front matter
- **Static**: SEO-friendly, fast loading, no server needed
- **Popular**: Large community, good documentation

### Template Engine

Nunjucks was chosen for:
- Powerful templating features (inheritance, includes, filters)
- Familiar syntax (similar to Jinja2, Liquid)
- Good documentation and examples

### Syntax Highlighting

Prism.js provides:
- Wide language support (Python, JavaScript, Bash, etc.)
- Theme customization
- Lightweight and fast

## Next Steps

- **Custom Domain**: Configure domain in hosting provider
- **SEO**: Add meta tags, sitemaps, robots.txt
- **Analytics**: Integrate Google Analytics or Plausible
- **Search**: Add Lunr.js or Algolia for site search
- **PWA**: Convert to Progressive Web App for offline access

---

## Handling Template Syntax Conflicts

### The Problem

Nunjucks (Eleventy's template engine) uses `{{ }}` and `{% %}` for templating. However, many frameworks also use these delimiters:

- **Vue.js**: `{{ message }}` for data binding
- **Angular**: `{{ expression }}` for interpolation
- **Jinja2/Django**: `{{ variable }}` in Python templates

When Eleventy processes markdown containing these syntaxes, it causes build failures:

```
[11ty] unexpected token: }}
```

### The Solution

The `CourseGenerator` automatically wraps problematic syntax with `{% raw %}...{% endraw %}` tags:

```python
# Automatically applied to all AI-generated content
markdown_content = self._wrap_template_syntax(markdown_content)
```

This method:
1. Detects `{{ }}` or `{% %}` in code blocks and inline code
2. Wraps them with `{% raw %}...{% endraw %}` tags
3. Preserves all formatting and indentation
4. Works for Vue, Angular, Jinja2, and similar frameworks

### Example

**Before** (causes errors):
```markdown
<div id="app">{{ message }}</div>
```

**After** (works correctly):
```markdown
{% raw %}
<div id="app">{{ message }}</div>
{% endraw %}
```

### Coverage

Applied to all content types:
- README (course overview)
- Lesson content
- Exercises and solutions
- Quick references
- Best practices

This ensures **all future courses work automatically** without manual fixes.

---

For more information about Eleventy, visit: https://www.11ty.dev/docs/
