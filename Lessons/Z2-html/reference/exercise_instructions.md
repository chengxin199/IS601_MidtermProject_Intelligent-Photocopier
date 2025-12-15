---
title: Introduction to html - Exercise Instructions
layout: layouts/course.njk
courseId: Z2-html
permalink: /Lessons/Z2-html/exercise-instructions.html
tags:
  - exercises
  - practice
date: 2025-12-15T22:42:37.718455
---
## Exercise 1: Basic HTML Structure
**Difficulty:** Beginner  
**Time Estimate:** 15 minutes  

### Objective
Create a simple HTML document with a proper structure including the `<html>`, `<head>`, and `<body>` tags. Include a title for the document and a heading in the body.

### Starter Code
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Title Here</title>  <!-- TODO: Set your title -->
</head>
<body>
    <h1>Your Heading Here</h1>  <!-- TODO: Set your main heading -->
</body>
</html>
```

### Requirements
- Set the title of the document to "My First HTML Page".
- Add a main heading in the body that says "Welcome to My First HTML Page".

### Test Cases
1. Check if the title tag contains "My First HTML Page".
2. Check if the `<h1>` tag contains "Welcome to My First HTML Page".

### Hints
- Remember to close all your HTML tags properly.
- Use a web browser to preview your HTML document.

---

## Exercise 2: Adding Lists and Links
**Difficulty:** Intermediate  
**Time Estimate:** 20 minutes  

### Objective
Enhance your HTML document by adding an unordered list and a hyperlink.

### Starter Code
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First HTML Page</title>
</head>
<body>
    <h1>Welcome to My First HTML Page</h1>
    
    <h2>My Favorite Fruits</h2>
    <ul>
        <!-- TODO: Add list items here -->
    </ul>

    <p>Visit <a href="https://example.com">Example Site</a>!</p>  <!-- TODO: Change link text -->
</body>
</html>
```

### Requirements
- Add an unordered list containing at least three of your favorite fruits.
- Change the link text inside the `<a>` tag to "Click Here".

### Test Cases
1. Check if the unordered list contains at least three `<li>` elements.
2. Check if the link text is "Click Here".

### Hints
- Use `<li>` tags for each item in your list.
- Make sure the hyperlink points to a valid URL.

---

## Exercise 3: Adding Images and Styling
**Difficulty:** Intermediate  
**Time Estimate:** 25 minutes  

### Objective
Introduce images and basic CSS styling to your HTML document.

### Starter Code
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First HTML Page</title>
    <style>
        /* TODO: Add CSS styles here */
    </style>
</head>
<body>
    <h1>Welcome to My First HTML Page</h1>
    
    <h2>My Favorite Fruits</h2>
    <ul>
        <li>Apple</li>
        <li>Banana</li>
        <li>Cherry</li>
    </ul>

    <img src="fruit.jpg" alt="A selection of fruits">  <!-- TODO: Replace with a valid image URL -->
</body>
</html>
```

### Requirements
- Add a CSS rule that changes the background color of the body to light blue.
- Replace the `src` attribute of the `<img>` tag with a valid image URL of your choice.

### Test Cases
1. Check if the body background color is light blue.
2. Check if the image loads correctly without any broken links.

### Hints
- Use the developer tools in your browser to inspect elements and test styles.
- Make sure the image URL is accessible.

---

## Exercise 4: Creating a Form
**Difficulty:** Intermediate  
**Time Estimate:** 30 minutes  

### Objective
Create a simple form in your HTML document to collect user information.

### Starter Code
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First HTML Page</title>
    <style>
        /* TODO: Add CSS styles here */
    </style>
</head>
<body>
    <h1>Welcome to My First HTML Page</h1>
    
    <h2>User Information Form</h2>
    <form action="#" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>  <!-- TODO: Ensure this is required -->

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>  <!-- TODO: Ensure this is required -->

        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

### Requirements
- Ensure the form has fields for name and email, both of which are required.
- Add a submit button that says "Submit".

### Test Cases
1. Check that the form does not submit if the name or email fields are empty.
2. Check that the form correctly submits when both fields are filled.

### Hints
- Use the `required` attribute on input elements to enforce validation.
- Test the form functionality by interacting with it in a browser.

---

These exercises will help students incrementally build their HTML skills while creating a real-world project.