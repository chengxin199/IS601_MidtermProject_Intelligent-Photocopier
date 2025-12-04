---
title: Third-Party Libraries - Exercise Instructions
layout: layouts/course.njk
courseId: C6-working-with-thirdparty-libraries
tags:
  - exercises
date: 2025-11-17T20:03:21.604104
---
## Exercise 1: Reading Documentation and Understanding Semantic Versioning

### Objective:
Learn how to read and interpret library documentation and understand semantic versioning.

### Instructions:
1. **Select a Library**: Visit a popular repository (e.g., npm for JavaScript, PyPI for Python, or Maven for Java) and choose a library of interest.
2. **Documentation Review**: Locate the documentation for the library. Focus on:
   - Overview: What does the library do?
   - Installation: How to install it?
   - Basic Usage: How to use its core features? 
3. **Semantic Versioning**: Identify the latest version of the library and check its version number. Write down the major, minor, and patch versions (e.g., 1.4.2).
   - What do the changes in the major version signify?
   - What about the minor and patch versions?
4. **Constraints/Markers**: Look for any constraints or markers in the documentation. Are there any specific compatibility notes or dependencies?

### Acceptance Criteria:
- A summary of the library's purpose and installation instructions.
- A clear explanation of the semantic versioning scheme and what the current version indicates.
- A list of any relevant constraints or markers noted in the documentation.

### Hints for Common Challenges:
- If you can’t find the documentation, try searching for “[library name] documentation” in your favorite search engine.
- Semantic versioning might be explained in a section about "Releases" or "Changelog."

---

## Exercise 2: Implementing a Minimal API with Adapter Pattern

### Objective:
Practice creating a minimal API that interacts with a third-party library while avoiding tight coupling using the adapter pattern.

### Instructions:
1. **Choose a Library**: Select a library that serves a specific purpose (like an HTTP client).
2. **Create an Adapter**: Write an adapter class that wraps around the library’s functionalities. For example, if you’re using an HTTP library, create an `HttpClientAdapter` class.
   - Your adapter should provide a minimal set of methods that your main application will use.
3. **Implement a Feature**: Use the adapter in a small application. For instance, create a simple application that makes a GET request to a public API (like a weather API) and returns the data in a user-friendly format.

### Acceptance Criteria:
- An adapter class that encapsulates the functionality of the selected library.
- A working application that utilizes the adapter to fetch and display data.

### Hints for Common Challenges:
- Ensure your adapter methods have clear and concise names that represent their functionality.
- If you encounter issues with the library, refer back to its documentation for examples and usage patterns.

---

## Exercise 3: Handling Deprecation and Basic Security Scanning

### Objective:
Learn how to handle deprecated methods in a library and perform basic security checks.

### Instructions:
1. **Use the Library**: Select a library that has documented deprecated methods (you can use the one from Exercise 1 or a new one).
2. **Identify Deprecation**: Write a small script that uses a deprecated feature of the library. 
3. **Update the Code**: Find the recommended alternative from the documentation and refactor your code to use the new method.
4. **Basic Security Scanning**: Use a tool (like `npm audit` for JavaScript or `bandit` for Python) to scan your project for security vulnerabilities. 
   - Address any issues that arise, either by updating the library or modifying your implementation.

### Acceptance Criteria:
- A script that initially uses a deprecated method and a refactored version that uses the new method.
- A summary report of security vulnerabilities found and how they were addressed.

### Hints for Common Challenges:
- If you can’t find information on deprecated methods, check the library’s changelog or issues section.
- Security scanning tools may require installation, so check the documentation for instructions.

---

## Exercise 4: Selecting and Justifying a Library Choice

### Objective:
Practice evaluating and justifying the selection of a third-party library for a specific feature.

### Instructions:
1. **Feature Selection**: Identify a feature you want to implement in your application (e.g., data formatting, CLI tools, or HTTP requests).
2. **Research Libraries**: Look for at least three different libraries that can implement this feature. Consider factors such as:
   - Popularity (Downloads, GitHub stars)
   - Documentation quality
   - Community support
   - Recent activity (Last updated date)
3. **Comparison Matrix**: Create a comparison matrix to evaluate the libraries based on the criteria above.
4. **Justification**: Write a short paragraph justifying your final library choice based on your evaluation.

### Acceptance Criteria:
- A comparison matrix detailing the libraries evaluated.
- A well-reasoned justification for the selected library.

### Hints for Common Challenges:
- Use websites like GitHub, npm, or PyPI to gauge popularity and community activity.
- Documentation can be subjective; consider ease of use and clarity as important factors.

---

## Exercise 5: Building and Testing a Feature Using Selected Library

### Objective:
Implement a feature using the selected library from Exercise 4, ensuring proper testing and usage.

### Instructions:
1. **Implementation**: Using the library you selected, implement the feature in your application. Ensure that your code adheres to best practices.
2. **Testing**: Write unit tests for your implementation. Ensure you cover:
   - Normal cases
   - Edge cases
   - Error handling
3. **Run Tests**: Execute your tests and ensure they all pass. Address any issues that arise.

### Acceptance Criteria:
- A functional feature implemented using the selected library.
- Comprehensive unit tests that cover the feature adequately.

### Hints for Common Challenges:
- Don’t hesitate to refer to the library’s documentation for examples while writing your implementation.
- If tests are failing, use debugging techniques to pinpoint the errors, such as printing variable values or using a debugger.

These exercises are designed to provide a comprehensive experience with third-party libraries, gradually building up the complexity and understanding needed to work effectively with external code.