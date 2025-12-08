---
title: introduction to big data - Practice Solution
layout: layouts/course.njk
courseId: B9-big-data
tags:
  - solutions
  - code
date: 2025-12-08T16:00:52.787274
---
# Introduction to Big Data - Practice Solution Document

This document provides a comprehensive overview of basic concepts related to Big Data through practical exercises. Each exercise will include a basic implementation, an enhanced version with error handling, and testing examples.

## Exercise 1: Data Aggregation

### Overview
Data aggregation is a fundamental concept in Big Data, involving the collection and summarization of data. In this exercise, we will create a simple program that aggregates sales data by product category.

### Basic Implementation

```python
# Basic implementation of data aggregation

def aggregate_sales(sales_data):
    """Aggregate sales data by product category."""
    # Initialize an empty dictionary to hold the aggregated results
    aggregated_data = {}
    
    # Loop through each sale in the sales data
    for sale in sales_data:
        category = sale['category']
        amount = sale['amount']
        
        # Aggregate sales amounts by category
        if category in aggregated_data:
            aggregated_data[category] += amount
        else:
            aggregated_data[category] = amount
            
    return aggregated_data

# Sample sales data
sales_data = [
    {'category': 'Electronics', 'amount': 200},
    {'category': 'Groceries', 'amount': 150},
    {'category': 'Electronics', 'amount': 300},
]

# Call the function and print the results
print(aggregate_sales(sales_data))
```

### Enhanced Implementation

```python
# Enhanced implementation with error handling

def aggregate_sales_enhanced(sales_data):
    """Aggregate sales data by product category with error handling."""
    # Initialize an empty dictionary to hold the aggregated results
    aggregated_data = {}
    
    # Loop through each sale in the sales data
    for sale in sales_data:
        # Validate that 'category' and 'amount' exist in sale
        if 'category' not in sale or 'amount' not in sale:
            raise ValueError("Each sale must contain 'category' and 'amount' keys.")
        
        # Validate that the amount is a number
        if not isinstance(sale['amount'], (int, float)):
            raise TypeError("Sales amount must be a number.")
        
        category = sale['category']
        amount = sale['amount']
        
        # Aggregate sales amounts by category
        if category in aggregated_data:
            aggregated_data[category] += amount
        else:
            aggregated_data[category] = amount
            
    return aggregated_data

# Sample sales data
sales_data = [
    {'category': 'Electronics', 'amount': 200},
    {'category': 'Groceries', 'amount': 150},
    {'category': 'Electronics', 'amount': 300},
]

# Call the function and print the results
print(aggregate_sales_enhanced(sales_data))
```

### Testing the Solution

```python
def test_aggregate_sales():
    """Unit test for the aggregate_sales function."""
    sales_data = [
        {'category': 'Electronics', 'amount': 200},
        {'category': 'Groceries', 'amount': 150},
        {'category': 'Electronics', 'amount': 300},
        {'category': 'Clothing', 'amount': 100}
    ]
    
    expected_output = {
        'Electronics': 500,
        'Groceries': 150,
        'Clothing': 100
    }
    
    assert aggregate_sales(sales_data) == expected_output
    print("Basic Implementation Test Passed.")

def test_aggregate_sales_enhanced():
    """Unit test for the aggregate_sales_enhanced function."""
    sales_data = [
        {'category': 'Electronics', 'amount': 200},
        {'category': 'Groceries', 'amount': 150},
        {'category': 'Electronics', 'amount': 300},
        {'category': 'Clothing', 'amount': 100}
    ]
    
    expected_output = {
        'Electronics': 500,
        'Groceries': 150,
        'Clothing': 100
    }
    
    assert aggregate_sales_enhanced(sales_data) == expected_output
    print("Enhanced Implementation Test Passed.")
    
    # Testing error handling
    try:
        aggregate_sales_enhanced([{'category': 'Electronics'}])  # Missing 'amount'
    except ValueError as e:
        assert str(e) == "Each sale must contain 'category' and 'amount' keys."
    
    try:
        aggregate_sales_enhanced([{'category': 'Electronics', 'amount': '200'}])  # Invalid amount
    except TypeError as e:
        assert str(e) == "Sales amount must be a number."
    
    print("Enhanced Implementation Error Handling Tests Passed.")

# Run tests
test_aggregate_sales()
test_aggregate_sales_enhanced()
```

### Explanation
- **Design Decisions**: The basic implementation focuses on simplicity, directly aggregating sales data without validation. The enhanced version includes error handling to ensure data integrity, raising appropriate exceptions for missing or invalid data.
- **Key Concepts**: This exercise reinforces the concepts of data aggregation, dictionary usage, and error handling in Python.
- **Complexity Analysis**: The time complexity of both implementations is O(n), where n is the number of sales records, as we traverse the list once.

### Key Takeaways
- Always validate input data to ensure correctness.
- Error handling is crucial in production code to avoid crashes and provide feedback.
- Understand the difference between basic and enhanced implementations—enhanced versions are more robust and suitable for real-world applications.