---
title: introduction to javascript - Quick Reference
layout: layouts/course.njk
courseId: J1-javascript-learn
tags:
  - reference
  - quick-guide
date: 2025-12-04T15:54:15.564089
---
# Introduction to JavaScript — Quick Reference Guide

---

## Course Overview
- **Duration:** 3-4 hours  
- **Level:** Intermediate  
- **Topics:**  
  - Introduction  
  - Core Concepts  
  - Advanced Techniques  
  - Best Practices  
  - Summary  

---

## 1. Key Concepts

### JavaScript Basics  
- **Variables:** Containers for data (`let`, `const`, `var`)  
- **Data Types:** Number, String, Boolean, Object, Array, Null, Undefined, Symbol  
- **Functions:** Reusable blocks of code  
- **Scope:** Where variables are accessible (`global`, `local`, `block`)  
- **Events:** Actions users or browsers trigger (e.g., clicks)  

### Core Concepts  
- **Hoisting:** Declarations are moved to the top of their scope  
- **Closures:** Functions that remember their lexical scope  
- **Asynchronous JS:** Callbacks, Promises, `async/await`  
- **DOM Manipulation:** Access and modify HTML elements via JS  

### Advanced Techniques  
- **Modules:** Import/export code across files  
- **Destructuring:** Extract values from arrays/objects  
- **Spread/Rest Operators:** Expand or collect elements  
- **Prototypes & Inheritance:** Object-oriented patterns  
- **Event Delegation:** Efficient event handling  

---

## 2. Common Patterns & Syntax Examples

### Variable Declaration  
```js
let name = 'Alice';       // Mutable variable  
const PI = 3.14;          // Immutable constant  
var count = 0;            // Function-scoped variable (avoid in modern code)
```

### Functions  
```js
// Function Declaration
function greet(name) {
  return `Hello, ${name}!`;
}

// Arrow Function
const add = (a, b) => a + b;
```

### Conditionals  
```js
if (score > 90) {
  console.log('Great job!');
} else if (score > 75) {
  console.log('Good effort!');
} else {
  console.log('Keep practicing.');
}
```

### Loops  
```js
for (let i = 0; i < 5; i++) {
  console.log(i);
}

const arr = [1, 2, 3];
arr.forEach(item => console.log(item));
```

### Objects & Arrays  
```js
const person = {
  name: 'Bob',
  age: 30,
  greet() {
    console.log('Hi!');
  }
};

const numbers = [10, 20, 30];
```

### Destructuring  
```js
const { name, age } = person;
const [first, second] = numbers;
```

### Async/Await  
```js
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    console.log(data);
  } catch (err) {
    console.error('Error:', err);
  }
}
```

---

## 3. Troubleshooting Quick Fixes

| Issue                          | Quick Fix / Tip                                      |
|-------------------------------|----------------------------------------------------|
| **`undefined` or `null` errors** | Check variable initialization and DOM element existence before use. Use optional chaining `obj?.prop`. |
| **`NaN` results in calculations** | Ensure inputs are numbers. Use `Number()` or `parseInt()` to convert strings. |
| **Scope issues (variables not accessible)** | Use `let` or `const` instead of `var`. Check block vs function scope. |
| **Event listeners not firing** | Confirm event is attached after DOM loads (`DOMContentLoaded`). Verify selector matches element. |
| **Promises not resolving** | Always handle `.catch()` or use `try/catch` with `async/await`. Verify API endpoints. |
| **Syntax errors** | Use linters (ESLint) and carefully check for missing brackets, commas, semicolons. |

---

## 4. Best Practices

- Use `const` by default; `let` only if reassignment needed. Avoid `var`.  
- Write pure functions (no side effects) where possible.  
- Use meaningful variable and function names.  
- Keep functions small and focused.  
- Use template literals for string interpolation: `` `Hello, ${name}!` ``  
- Handle errors gracefully with `try/catch`.  
- Comment complex logic clearly.  
- Avoid polluting global scope (use modules or IIFE).  
- Use strict equality (`===`) instead of loose (`==`).  
- Prefer `forEach`, `map`, `filter` over traditional loops for arrays.  

---

## 5. Summary Cheat Sheet

| Concept               | Example / Syntax                              |
|-----------------------|----------------------------------------------|
| Declare variable      | `let x = 10; const y = 20;`                   |
| Function declaration  | `function foo() { return 'bar'; }`            |
| Arrow function       | `const sum = (a,b) => a + b;`                  |
| Object literal       | `const obj = {a:1, b:2};`                      |
| Array literal        | `const arr = [1, 2, 3];`                       |
| Destructuring        | `const {a, b} = obj; const [x, y] = arr;`     |
| Async function       | `async function fetch() { await ... }`         |
| Event listener       | `element.addEventListener('click', handler);` |
| Template literals    | `` `Hello, ${name}!` ``                         |
| Spread operator      | `const newArr = [...arr, 4];`                   |
| Rest parameters      | `function sum(...nums) {}`                       |

---

Keep this guide handy during coding sessions for quick reminders and fixes! Happy coding! 🚀