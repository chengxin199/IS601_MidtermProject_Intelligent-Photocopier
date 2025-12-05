---
title: Vue introduction - Quick Reference
layout: layouts/course.njk
courseId: V1-vue-introduction
tags:
  - reference
  - quick-guide
date: 2025-12-05T01:38:53.938072
---
# Vue.js Quick Reference Guide

## Course Overview
- **Duration**: 3-4 hours
- **Level**: Intermediate

---

## 1. Introduction to Vue.js
- **What is Vue.js?**
  - A progressive JavaScript framework for building user interfaces.
  - Focuses on the view layer and is easy to integrate with other projects.

- **Key Features**:
  - Reactive data binding
  - Component-based architecture
  - Virtual DOM for performance optimization

---

## 2. Core Concepts

### 2.1 Vue Instance
- **Creating a Vue Instance**:
  ```javascript
  const app = new Vue({
    el: '#app',
    data: {
      message: 'Hello Vue!'
    }
  });
  ```

### 2.2 Data Binding
- **Interpolation**:
{% raw %}
  ```html
  <div id="app">{{ message }}</div>
  ```
{% endraw %}

- **v-bind Directive**:
  ```html
  <img v-bind:src="imageSrc">
  ```

### 2.3 Directives
- **Common Directives**:
  - `v-if`: Conditionally render elements.
  - `v-for`: Render a list of items.
  - `v-model`: Two-way data binding for form inputs.

### 2.4 Components
- **Defining a Component**:
  ```javascript
  Vue.component('my-component', {
    template: '<div>A custom component!</div>'
  });
  ```

- **Using a Component**:
  ```html
  <my-component></my-component>
  ```

---

## 3. Advanced Techniques

### 3.1 Vue Router
- **Setting Up Router**:
  ```javascript
  const router = new VueRouter({
    routes: [
      { path: '/home', component: HomeComponent },
      { path: '/about', component: AboutComponent }
    ]
  });
  ```

### 3.2 Vuex (State Management)
- **Store Setup**:
  ```javascript
  const store = new Vuex.Store({
    state: {
      count: 0
    },
    mutations: {
      increment(state) {
        state.count++;
      }
    }
  });
  ```

### 3.3 Mixins
- **Creating a Mixin**:
  ```javascript
  const myMixin = {
    data() {
      return {
        mixinData: 'Mixin data'
      };
    }
  };
  ```

---

## 4. Best Practices

- **Component Naming**:
  - Use PascalCase for component names.

- **Keep Components Small**:
  - Aim for single responsibility; each component should do one thing.

- **Use Vue Devtools**:
  - Install Vue Devtools for better debugging and state management.

---

## 5. Troubleshooting Quick Fixes

### Common Issues
- **Vue Instance Not Updating**:
  - Ensure data properties are reactive. Use `Vue.set()` for adding new properties.

- **Component Not Rendering**:
  - Check if the component is registered correctly and the template is valid.

- **Event Handling Issues**:
  - Ensure methods are defined in the `methods` section of the Vue instance.

### Console Errors
- **[Vue warn]: Error in render**:
  - Check for typos in template bindings or missing data properties.

- **[Vue warn]: Failed to mount component**:
  - Ensure the component is registered and that the mounting point exists in the DOM.

---

## Summary
- Vue.js is a versatile framework for building interactive web applications.
- Focus on understanding core concepts like the Vue instance, directives, and components.
- Leverage advanced features like Vue Router and Vuex for larger applications.
- Follow best practices to maintain clean and efficient code.
- Utilize troubleshooting tips to quickly resolve common issues.

---

Keep this guide handy while coding to reinforce your understanding of Vue.js concepts and practices!
