---
title: Vue introduction - Exercise Instructions
layout: layouts/course.njk
courseId: V1-vue-introduction
tags:
  - exercises
  - practice
date: 2025-12-05T01:39:49.275978
---
## Exercise 1: Vue Instance Creation
**Difficulty:** Beginner  
**Time Estimate:** 20 minutes

### Objective
Create a simple Vue instance that displays a message on the webpage.

### Starter Code
```html
<!DOCTYPE html>
<html>
<head>
    <title>Vue Instance</title>
    <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
</head>
<body>
    <div id="app">
        <!-- TODO: Display the message here -->
    </div>

    <script>
        // TODO: Create a new Vue instance
        var app = new Vue({
            el: '#app',
            data: {
                message: 'Hello Vue!'
            }
        });
    </script>
</body>
</html>
```

### Requirements
- Display the `message` variable inside the `<div id="app">`.
- Change the `message` to "Welcome to Vue!" and ensure it updates on the webpage.

### Test Cases
To validate your implementation, check that the displayed content matches the expected message:
1. Open the HTML file in a browser; the text should be "Hello Vue!" initially.
2. Change the value of `message` to "Welcome to Vue!" and verify that it updates accordingly.

### Hints
- Use double curly braces `{{ }}` to bind data in Vue templates.
- Make sure your Vue instance is correctly linked to the HTML element ID.

---

## Exercise 2: Data Binding
**Difficulty:** Intermediate  
**Time Estimate:** 30 minutes

### Objective
Implement data binding to create an input field that updates the displayed message in real-time.

### Starter Code
```html
<!DOCTYPE html>
<html>
<head>
    <title>Vue Data Binding</title>
    <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
</head>
<body>
    <div id="app">
        <input type="text" placeholder="Type a message" v-model="message">
        <p>Your message: {{ message }}</p>
    </div>

    <script>
        // TODO: Create a new Vue instance
        var app = new Vue({
            el: '#app',
            data: {
                message: '' // TODO: Initialize an empty message
            }
        });
    </script>
</body>
</html>
```

### Requirements
- Use the `v-model` directive to bind the input field to the `message` variable.
- Ensure that as the user types in the input field, the displayed message updates in real-time.

### Test Cases
1. Start with an empty input field. The paragraph should initially say "Your message: ".
2. Type "Hello" into the input field. The paragraph should update to "Your message: Hello".

### Hints
- Remember that `v-model` creates a two-way data binding between the input and the Vue instance.
- Check for syntax errors if your data binding does not work as expected.

---

## Exercise 3: Conditional Rendering
**Difficulty:** Intermediate  
**Time Estimate:** 35 minutes

### Objective
Implement conditional rendering to show a special message when the input field contains a specific keyword.

### Starter Code
```html
<!DOCTYPE html>
<html>
<head>
    <title>Vue Conditional Rendering</title>
    <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
</head>
<body>
    <div id="app">
        <input type="text" placeholder="Type a message" v-model="message">
        <p>Your message: {{ message }}</p>
        <!-- TODO: Show a special message when input is "Vue" -->
        <p v-if="message === 'Vue'">You typed the keyword!</p>
    </div>

    <script>
        // TODO: Create a new Vue instance
        var app = new Vue({
            el: '#app',
            data: {
                message: ''
            }
        });
    </script>
</body>
</html>
```

### Requirements
- Use the `v-if` directive to conditionally render a message when the input is exactly "Vue".
- Ensure that the special message disappears when the input changes to anything else.

### Test Cases
1. Type "Hello" into the input field. The special message should not appear.
2. Change the input to "Vue". The special message "You typed the keyword!" should now be visible.
3. Change the input to "VueJS". The special message should disappear.

### Hints
- Be mindful of using strict equality (`===`) for comparisons in Vue directives.
- Use the browser console for debugging if the conditional rendering doesn’t work as expected.

---

## Exercise 4: List Rendering
**Difficulty:** Intermediate  
**Time Estimate:** 40 minutes

### Objective
Create a list of items and render them dynamically using Vue's `v-for` directive.

### Starter Code
```html
<!DOCTYPE html>
<html>
<head>
    <title>Vue List Rendering</title>
    <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
</head>
<body>
    <div id="app">
        <ul>
            <!-- TODO: Render the items from the 'items' array -->
        </ul>
        <input type="text" v-model="newItem" placeholder="Add a new item">
        <button @click="addItem">Add Item</button>
    </div>

    <script>
        var app = new Vue({
            el: '#app',
            data: {
                items: ['Item 1', 'Item 2', 'Item 3'], // TODO: Initial list of items
                newItem: ''
            },
            methods: {
                addItem: function() {
                    // TODO: Implement the logic to add newItem to items
                }
            }
        });
    </script>
</body>
</html>
```

### Requirements
- Use `v-for` to render the items from the `items` array inside the `<ul>`.
- Implement the `addItem` method to push `newItem` into the `items` array when the button is clicked. Clear the input field afterward.

### Test Cases
1. Initially, the list should display "Item 1", "Item 2", and "Item 3".
2. Type "Item 4" in the input field and click the "Add Item" button. The list should now include "Item 4".
3. Ensure that the input field is cleared after adding an item.

### Hints
- Use the `@click` event to handle button clicks in Vue.
- Remember to use `this.items.push(this.newItem)` inside the method to update the data.

---

These exercises will allow students to progressively build their understanding of Vue.js, applying key concepts and techniques while working towards a real-world project.