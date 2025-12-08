---
title: introduce to html and css - Quick Reference
layout: layouts/course.njk
courseId: z1-html-css
permalink: /Lessons/z1-html-css/quick-reference.html
tags:
  - reference
  - quick-guide
date: 2025-12-08T18:49:49.071087
---
# Quick Reference Guide: Introduction to HTML and CSS

## Course Overview
- **Duration**: 3-4 hours
- **Level**: Intermediate
- **Topics**: 
  - Introduction
  - Core Concepts
  - Advanced Techniques
  - Best Practices
  - Summary

---

## 1. Introduction
HTML (HyperText Markup Language) and CSS (Cascading Style Sheets) are the foundational technologies for creating web pages.

### Key Concepts
- **HTML**: Structure of web content.
- **CSS**: Presentation and layout of web content.

---

## 2. Core Concepts

### HTML Basics
- **Elements**: Building blocks of HTML (e.g., `<div>`, `<p>`, `<a>`).
- **Attributes**: Provide additional information (e.g., `href`, `src`).
  
#### Example:
```html
<a href="https://www.example.com">Visit Example</a>
```

### CSS Basics
- **Selectors**: Target HTML elements (e.g., `element`, `.class`, `#id`).
- **Properties**: Styles applied to elements (e.g., `color`, `font-size`).

#### Example:
```css
h1 {
    color: blue;
    font-size: 24px;
}
```

---

## 3. Advanced Techniques

### Responsive Design
- Use **media queries** to adapt styles based on device size.

#### Example:
```css
@media (max-width: 600px) {
    body {
        background-color: lightblue;
    }
}
```

### Flexbox Layout
- A layout model that allows responsive alignment of elements.

#### Example:
```css
.container {
    display: flex;
    justify-content: space-between;
}
```

### Grid Layout
- A two-dimensional layout system.

#### Example:
```css
.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
}
```

---

## 4. Best Practices

### HTML
- Use semantic tags (`<header>`, `<footer>`, `<article>`) for better SEO and accessibility.
- Ensure all images have `alt` attributes.

### CSS
- Keep styles modular and organized.
- Use a CSS reset or normalize stylesheet to ensure consistency across browsers.

### Version Control
- Use Git for version control to track changes and collaborate effectively.

---

## 5. Troubleshooting Quick Fixes

### Common Issues
- **Element Not Displaying**: Check if it’s hidden by CSS (`display: none;`).
- **Styles Not Applying**: Ensure specificity is correct; check for typos in selectors.

### Debugging Tools
- Use browser developer tools (F12) to inspect elements and view applied styles.

### Clear Cache
- If changes don’t appear, clear browser cache or use incognito mode to see updates.

---

## Summary
- **HTML** defines structure; **CSS** defines style.
- Use semantic HTML for better accessibility and SEO.
- Utilize responsive design techniques for a better user experience.
- Keep code organized and leverage version control for collaboration.

This guide serves as a quick reference to help you navigate HTML and CSS effectively during your coding sessions.