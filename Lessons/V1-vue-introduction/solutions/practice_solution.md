---
title: Vue introduction - Practice Solution
layout: layouts/course.njk
courseId: V1-vue-introduction
tags:
  - solutions
  - code
date: 2025-12-05T01:40:11.918078
---
# Vue Introduction Practice Solution Document

## Learning Objectives
- Master key concepts of Vue.js.
- Apply practical techniques in building Vue components.
- Build real-world projects using Vue.js.

---

## Exercise 1: Creating a Simple Vue Component

### Overview
In this exercise, we will create a simple Vue.js component that displays a message and a button to update that message. We will start with a basic implementation and then enhance it with error handling.

### Basic Implementation

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vue Introduction</title>
    <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
</head>
<body>
    <div id="app">
        <message-component></message-component>
    </div>

    <script>
        // Define a new Vue component called 'message-component'
        Vue.component('message-component', {
            data: function() {
                return {
                    message: 'Hello, Vue!'
                };
            },
{% raw %}            template: `
                <div>
                    <p>{{ message }}</p>
                    <button @click="updateMessage">Update Message</button>
                </div>
            `,{% endraw %}
            methods: {
                // Method to update the message
                updateMessage() {
                    this.message = 'You clicked the button!';
                }
            }
        });

        // Create a new Vue instance
        new Vue({
            el: '#app'
        });
    </script>
</body>
</html>
```

### Enhanced Implementation

```html
<!-- Enhanced version with error handling -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vue Introduction Enhanced</title>
    <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
</head>
<body>
    <div id="app">
        <message-component></message-component>
    </div>

    <script>
        Vue.component('message-component', {
            data: function() {
                return {
                    message: 'Hello, Vue!',
                    error: null
                };
            },
{% raw %}            template: `
                <div>
                    <p v-if="error" style="color: red;">{{ error }}</p>
                    <p v-else>{{ message }}</p>
                    <button @click="updateMessage">Update Message</button>
                </div>
            `,{% endraw %}
            methods: {
                updateMessage() {
                    try {
                        // Simulate a potential error
                        if (Math.random() < 0.5) {
                            throw new Error('Failed to update message');
                        }
                        this.message = 'You clicked the button!';
                        this.error = null; // Clear any previous error
                    } catch (err) {
                        this.error = err.message; // Set the error message
                    }
                }
            }
        });

        new Vue({
            el: '#app'
        });
    </script>
</body>
</html>
```

### Testing the Solution

To test the functionality of our Vue component, we can simulate button clicks and verify the expected output. In a real application, you might use a testing framework like Jest, but for the sake of simplicity, we will define simple tests here.

```javascript
// Test cases for the Vue component
function testMessageComponent() {
    // Create the instance of the Vue component
    const vm = new Vue({ el: '#app' });

    // Initial message should be 'Hello, Vue!'
    console.assert(vm.$children[0].message === 'Hello, Vue!', 'Initial message is incorrect');

    // Simulate a button click to update the message
    vm.$children[0].updateMessage();

    // Check if the message has been updated
    console.assert(vm.$children[0].message === 'You clicked the button!', 'Message did not update correctly');
}

// Run the test function
testMessageComponent();
```

### Explanation
1. **Component Structure**: We defined a Vue component with a data function that returns an object containing the message and an error property.
2. **Template**: The template conditionally displays either an error message or the main message, depending on the state.
3. **Methods**: The `updateMessage` method updates the message and handles errors using a try-catch block.
4. **Testing**: We created a simple testing function to assert the correctness of the component's behavior.

### Key Takeaways
- Understanding Vue.js component structure is crucial for building applications.
- Error handling improves user experience by providing feedback.
- Testing components helps ensure reliability and correctness in functionality.

---

This document provides a solid foundation for understanding Vue.js components, their implementation, enhancement for error handling, and basic testing methodologies. By practicing these concepts, learners can effectively build robust web applications.
