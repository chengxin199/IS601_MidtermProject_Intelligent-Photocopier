---
title: introduce to html and css - Practice Solution
layout: layouts/course.njk
courseId: z1-html-css
permalink: /Lessons/z1-html-css/practice-solution.html
tags:
  - solutions
  - code
date: 2025-12-08T18:51:21.139065
---
# Introduction to HTML and CSS - Practice Solution Document

## Learning Objectives
- Master key concepts of HTML and CSS
- Apply practical techniques to build web pages
- Build real-world projects using HTML and CSS

---

## Exercise 1: Create a Basic HTML Page

### Overview
In this exercise, we will create a basic HTML page that includes a header, a paragraph, and a footer. The goal is to understand the structure of an HTML document.

### Basic Implementation

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Web Page</title>
    <link rel="stylesheet" href="styles.css"> <!-- Linking the CSS file -->
</head>
<body>
    <header>
        <h1>Welcome to My First Web Page</h1> <!-- Main title of the page -->
    </header>
    <main>
        <p>This is a paragraph of text on my first web page.</p> <!-- Content paragraph -->
    </main>
    <footer>
        <p>&copy; 2023 My First Web Page</p> <!-- Footer content -->
    </footer>
</body>
</html>
```

### Enhanced Implementation
In this enhanced version, we will add basic validation to ensure that our HTML structure is correct.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Web Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to My First Web Page</h1>
    </header>
    <main>
        <p>This is a paragraph of text on my first web page.</p>
    </main>
    <footer>
        <p>&copy; 2023 My First Web Page</p>
    </footer>

    <script>
        // Basic validation to check if the document is properly structured
        document.addEventListener("DOMContentLoaded", function() {
            if (!document.querySelector('h1')) {
                console.error("Error: Header (h1) is missing!");
            } else {
                console.log("Page loaded successfully.");
            }
        });
    </script>
</body>
</html>
```

### Testing the Solution
To test the HTML structure, open the HTML file in a web browser and ensure that the header, paragraph, and footer display correctly. 

To check for errors, open the browser’s console (F12 or right-click → Inspect → Console) and verify that there are no error messages.

### Explanation
- **Key Concepts**: Understanding the basic structure of an HTML document, including the `doctype`, `html`, `head`, and `body` elements.
- **Design Decisions**: The use of semantic HTML tags such as `header`, `main`, and `footer` to improve readability and accessibility.
- **Complexity Analysis**: The complexity of this implementation is O(1) since it involves a constant amount of work regardless of input size.

### Key Takeaways
- HTML documents must have a proper structure to function correctly.
- Semantic HTML improves accessibility and maintainability.
- Basic validation can help catch errors early in the development process.

---

## Exercise 2: Style the HTML Page with CSS

### Overview
In this exercise, we will add CSS to style our HTML page. This includes setting colors, fonts, spacing, and layout.

### Basic Implementation

```css
/* styles.css */
body {
    font-family: Arial, sans-serif; /* Setting the font family */
    margin: 0; /* Remove default margin */
    padding: 20px; /* Add padding */
    background-color: #f4f4f4; /* Light background color */
}

header {
    background: #35424a; /* Header background color */
    color: #ffffff; /* Header text color */
    padding: 20px; /* Header padding */
    text-align: center; /* Center align text */
}

footer {
    text-align: center; /* Center align footer text */
    margin-top: 20px; /* Space above footer */
}
```

### Enhanced Implementation
In the enhanced version, we'll add error handling for loading the CSS file and ensure styles are applied correctly.

```css
/* styles.css */
body {
    font-family: Arial, sans-serif; 
    margin: 0; 
    padding: 20px; 
    background-color: #f4f4f4; 
}

header {
    background: #35424a; 
    color: #ffffff; 
    padding: 20px; 
    text-align: center; 
}

footer {
    text-align: center; 
    margin-top: 20px; 
}

/* Additional styles for error handling */
.error {
    color: red; /* Error messages in red */
    font-weight: bold; /* Bold error messages */
}
```

```html
<!-- In the HTML file, add the following script to handle CSS loading -->
<script>
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'styles.css';
    
    link.onload = function() {
        console.log("CSS loaded successfully.");
    };
    
    link.onerror = function() {
        const errorMsg = document.createElement('div');
        errorMsg.className = 'error';
        errorMsg.innerText = "Error: CSS file failed to load.";
        document.body.prepend(errorMsg); // Add error message to the top of the page
    };
    
    document.head.appendChild(link);
</script>
```

### Testing the Solution
To test the CSS implementation, open the HTML file in a web browser. Make sure the styles are applied as expected by inspecting elements.

To test the error handling, you can temporarily change the `href` of the CSS link to an incorrect path and observe if the error message appears at the top of the page.

### Explanation
- **Key Concepts**: CSS selectors, properties, and the box model are essential for styling web pages.
- **Design Decisions**: Using external CSS for better separation of concerns between content (HTML) and presentation (CSS).
- **Complexity Analysis**: The complexity of rendering the styles is O(n), where n is the number of elements styled.

### Key Takeaways
- Proper styling enhances user experience and design.
- Error handling for resources like CSS files is critical for delivering a seamless experience.
- External stylesheets help maintain a clean structure and allow for reusability.

---

## Conclusion
This document provided a structured approach to mastering HTML and CSS through practical exercises. Each exercise demonstrated basic and enhanced implementations, detailed explanations, and testing strategies to ensure the code is robust and production-ready. Following these practices will help you build well-structured, styled web pages effectively.