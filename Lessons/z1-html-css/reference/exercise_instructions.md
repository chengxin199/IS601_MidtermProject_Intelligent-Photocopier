---
title: introduce to html and css - Exercise Instructions
layout: layouts/course.njk
courseId: z1-html-css
permalink: /Lessons/z1-html-css/exercise-instructions.html
tags:
  - exercises
  - practice
date: 2025-12-08T18:50:55.860566
---
## Exercise 1: Building a Basic HTML Structure
**Difficulty:** Beginner  
**Time Estimate:** 20 minutes

### Objective
In this exercise, you will create a simple HTML document structure. The document should include a title, a header, a paragraph, and a footer.

### Starter Code
```python
# Provide actual code template with TODO markers
def create_html_document():
    html_structure = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My First Web Page</title>
    </head>
    <body>
        <header>
            <h1>Welcome to My Web Page</h1>
        </header>
        <main>
            <p>This is a simple web page created with HTML.</p>
        </main>
        <footer>
            <p>© 2023 Your Name</p>
        </footer>
    </body>
    </html>
    """
    # TODO: Return the HTML document as a string
    return html_structure
```

### Requirements
- The document should be structured with a `header`, `main`, and `footer`.
- Include a `<title>` tag with a meaningful title.
- Ensure the HTML is properly formatted and indented.

### Test Cases
```python
# Example test cases
html_output = create_html_document()
assert "<title>My First Web Page</title>" in html_output
assert "<h1>Welcome to My Web Page</h1>" in html_output
assert "<p>This is a simple web page created with HTML.</p>" in html_output
```

### Hints
- Make sure you follow the correct HTML syntax.
- Use triple quotes for multi-line strings in Python.

---

## Exercise 2: Adding CSS Styles
**Difficulty:** Intermediate  
**Time Estimate:** 30 minutes

### Objective
Enhance your HTML document by adding basic CSS styles. You will style the header, paragraph, and footer elements.

### Starter Code
```python
def create_html_document_with_css():
    html_structure = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Styled Web Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            header {
                background: #35424a;
                color: white;
                padding: 10px 0;
                text-align: center;
            }
            footer {
                background: #35424a;
                color: white;
                text-align: center;
                padding: 10px 0;
                position: absolute;
                bottom: 0;
                width: 100%;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to My Styled Web Page</h1>
        </header>
        <main>
            <p>This is a simple web page created with HTML and styled with CSS.</p>
        </main>
        <footer>
            <p>© 2023 Your Name</p>
        </footer>
    </body>
    </html>
    """
    # TODO: Return the HTML document with CSS styles
    return html_structure
```

### Requirements
- Apply CSS styles to the `header`, `footer`, and `body`.
- Ensure the footer sticks to the bottom of the page.
- Use a background color for the body.

### Test Cases
```python
html_output = create_html_document_with_css()
assert "background-color: #f4f4f4;" in html_output
assert "color: white;" in html_output
assert "text-align: center;" in html_output
```

### Hints
- Use CSS properties like `background`, `color`, and `text-align`.
- Remember to place the `<style>` tag inside the `<head>` section.

---

## Exercise 3: Creating a Navigation Menu
**Difficulty:** Intermediate  
**Time Estimate:** 25 minutes

### Objective
Add a navigation menu to your HTML document using an unordered list. Style the menu with CSS to make it horizontal.

### Starter Code
```python
def create_html_with_navigation():
    html_structure = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Web Page with Navigation</title>
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            nav {
                background: #35424a;
                color: white;
                padding: 10px;
            }
            nav ul {
                list-style-type: none;
                display: flex;
                justify-content: space-around;
                padding: 0;
            }
            nav ul li {
                padding: 10px;
            }
        </style>
    </head>
    <body>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Services</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
        <main>
            <h1>Welcome to My Web Page</h1>
            <p>This is a simple web page created with HTML and styled with CSS.</p>
        </main>
        <footer>
            <p>© 2023 Your Name</p>
        </footer>
    </body>
    </html>
    """
    # TODO: Return the HTML document with navigation
    return html_structure
```

### Requirements
- Create a `nav` element containing an unordered list (`<ul>`) with at least four list items (`<li>`).
- Style the list to display horizontally.
- Ensure links have a default color that complements the header.

### Test Cases
```python
html_output = create_html_with_navigation()
assert "<nav>" in html_output
assert "<ul>" in html_output
assert "display: flex;" in html_output
```

### Hints
- Use `display: flex;` on the `<ul>` to align items horizontally.
- Remember to style the `<a>` tags for better visibility.

---

## Exercise 4: Responsive Design with Media Queries
**Difficulty:** Advanced  
**Time Estimate:** 40 minutes

### Objective
Make your web page responsive by using media queries in CSS. The layout should adjust for mobile and desktop views.

### Starter Code
```python
def create_responsive_html():
    html_structure = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Responsive Web Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
            }
            nav {
                background: #35424a;
                padding: 10px;
            }
            nav ul {
                list-style-type: none;
                display: flex;
                justify-content: space-around;
                padding: 0;
            }
            @media (max-width: 600px) {
                nav ul {
                    flex-direction: column;
                    align-items: center;
                }
            }
        </style>
    </head>
    <body>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Services</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
        <main>
            <h1>Welcome to My Responsive Web Page</h1>
            <p>This page adjusts its layout based on the screen size.</p>
        </main>
        <footer>
            <p>© 2023 Your Name</p>
        </footer>
    </body>
    </html>
    """
    # TODO: Return the responsive HTML document
    return html_structure
```

### Requirements
- Use media queries to change the layout of the navigation menu for devices with a screen width of 600px or less.
- Ensure that the menu items stack vertically in mobile view.
- Maintain readability and usability on all devices.

### Test Cases
```python
html_output = create_responsive_html()
assert "@media (max-width: 600px)" in html_output
assert "flex-direction: column;" in html_output
```

### Hints
- Test your design by resizing your browser window or using developer tools for mobile view.
- Use `flex-direction: column;` to stack navigation items vertically.

---

These exercises guide students through progressively complex tasks, from creating a simple HTML document to implementing responsive design, thereby enhancing their understanding of HTML and CSS.