---
title: introduction to big data - Practice Solution
layout: layouts/course.njk
courseId: B9-big-data
tags:
  - solutions
  - code
date: 2025-12-08T15:29:44.898170
---
# Introduction to Big Data - Practice Solutions

This document provides a comprehensive set of exercises focused on introducing big data concepts. You will find solutions that emphasize key concepts, practical techniques, and real-world project building.

## Table of Contents
1. [Exercise 1: Data Loading](#exercise-1-data-loading)
2. [Exercise 2: Data Transformation](#exercise-2-data-transformation)
3. [Exercise 3: Data Analysis](#exercise-3-data-analysis)
4. [Exercise 4: Data Visualization](#exercise-4-data-visualization)

---

## Exercise 1: Data Loading

### Overview
Data loading is the first step in any data processing pipeline. This exercise will focus on loading a CSV file into a pandas DataFrame, which is a common format for big data analysis.

### Basic Implementation
```python
import pandas as pd

def load_data(file_path):
    """Load data from a CSV file into a Pandas DataFrame."""
    # Read the CSV file
    data = pd.read_csv(file_path)
    return data

# Example usage
if __name__ == "__main__":
    df = load_data('data.csv')
    print(df.head())  # Display the first few rows of the DataFrame
```

### Enhanced Implementation
```python
import pandas as pd
import os

def load_data(file_path):
    """Load data from a CSV file into a Pandas DataFrame with error handling."""
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    try:
        # Read the CSV file
        data = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        raise ValueError("No data found in the CSV file.")
    except pd.errors.ParserError:
        raise ValueError("Error parsing the CSV file.")
    
    return data

# Example usage
if __name__ == "__main__":
    try:
        df = load_data('data.csv')
        print(df.head())
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Testing the Solution
```python
def test_load_data():
    """Test the load_data function with various cases."""
    # Test with a valid file
    try:
        df = load_data('test_data.csv')
        assert not df.empty, "DataFrame should not be empty."
    except Exception as e:
        print(f"Test failed: {e}")

    # Test with a non-existent file
    try:
        load_data('non_existent_file.csv')
    except FileNotFoundError as e:
        assert str(e) == "The file non_existent_file.csv does not exist."

    # Test with an empty file
    try:
        load_data('empty_file.csv')
    except ValueError as e:
        assert str(e) == "No data found in the CSV file."

# Uncomment to run tests
# test_load_data()
```

### Explanation
- **Design Decisions**: We used pandas for data handling due to its efficiency and ease of use. Error handling ensures that users are informed of issues.
- **Complexity Analysis**: The loading function runs in O(n) time complexity, where n is the number of rows in the CSV file, as it needs to read all data.

### Key Takeaways
- Always validate file paths and handle exceptions gracefully.
- Utilize libraries like pandas for efficient data manipulation.

---

## Exercise 2: Data Transformation

### Overview
Transforming data is crucial for preparing it for analysis. This exercise focuses on filtering and aggregating data.

### Basic Implementation
```python
def filter_data(data, column_name, threshold):
    """Filter data based on a threshold value for a specified column."""
    filtered_data = data[data[column_name] > threshold]
    return filtered_data

# Example usage
if __name__ == "__main__":
    df = load_data('data.csv')
    filtered_df = filter_data(df, 'column1', 100)
    print(filtered_df)
```

### Enhanced Implementation
```python
def filter_data(data, column_name, threshold):
    """Filter data with error handling for column existence."""
    if column_name not in data.columns:
        raise ValueError(f"Column {column_name} does not exist in the DataFrame.")

    filtered_data = data[data[column_name] > threshold]
    return filtered_data

# Example usage
if __name__ == "__main__":
    try:
        df = load_data('data.csv')
        filtered_df = filter_data(df, 'column1', 100)
        print(filtered_df)
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Testing the Solution
```python
def test_filter_data():
    """Test the filter_data function with various cases."""
    df = pd.DataFrame({
        'column1': [50, 150, 200],
        'column2': [1, 2, 3]
    })
    
    # Test filtering
    filtered_df = filter_data(df, 'column1', 100)
    assert len(filtered_df) == 2, "Filtered DataFrame should have 2 rows."

    # Test with non-existent column
    try:
        filter_data(df, 'non_existent_column', 100)
    except ValueError as e:
        assert str(e) == "Column non_existent_column does not exist in the DataFrame."

# Uncomment to run tests
# test_filter_data()
```

### Explanation
- **Design Decisions**: The function checks if the specified column exists before filtering, preventing runtime errors.
- **Complexity Analysis**: Filtering runs in O(n) time complexity, where n is the number of rows in the DataFrame.

### Key Takeaways
- Always verify the presence of columns before performing operations.
- Use vectorized operations in pandas for better performance.

---

## Exercise 3: Data Analysis

### Overview
This exercise focuses on calculating summary statistics from the data, which is essential for understanding data distributions.

### Basic Implementation
```python
def summarize_data(data):
    """Return summary statistics of the DataFrame."""
    summary = data.describe()
    return summary

# Example usage
if __name__ == "__main__":
    df = load_data('data.csv')
    summary_stats = summarize_data(df)
    print(summary_stats)
```

### Enhanced Implementation
```python
def summarize_data(data):
    """Return summary statistics with error handling for empty DataFrame."""
    if data.empty:
        raise ValueError("DataFrame is empty. Cannot compute summary statistics.")
    
    summary = data.describe()
    return summary

# Example usage
if __name__ == "__main__":
    try:
        df = load_data('data.csv')
        summary_stats = summarize_data(df)
        print(summary_stats)
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Testing the Solution
```python
def test_summarize_data():
    """Test the summarize_data function with various cases."""
    df = pd.DataFrame({
        'column1': [10, 20, 30],
        'column2': [5, 15, 25]
    })
    
    # Test summary statistics
    summary = summarize_data(df)
    assert 'column1' in summary.columns, "Summary should include column1."
    
    # Test with empty DataFrame
    empty_df = pd.DataFrame()
    try:
        summarize_data(empty_df)
    except ValueError as e:
        assert str(e) == "DataFrame is empty. Cannot compute summary statistics."

# Uncomment to run tests
# test_summarize_data()
```

### Explanation
- **Design Decisions**: The function checks for an empty DataFrame to avoid unnecessary computations and exceptions.
- **Complexity Analysis**: The summary statistics function runs in O(n) time complexity for n rows, as it needs to compute statistics for all values.

### Key Takeaways
- Utilize pandas' built-in methods for efficient statistical summaries.
- Handle edge cases like empty DataFrames to ensure robustness.

---

## Exercise 4: Data Visualization

### Overview
Visualizing data helps in understanding patterns and insights. This exercise will focus on creating basic visualizations with matplotlib.

### Basic Implementation
```python
import matplotlib.pyplot as plt

def plot_data(data, column_name):
    """Plot a histogram of the specified column."""
    plt.hist(data[column_name], bins=10)
    plt.title(f'Histogram of {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.show()

# Example usage
if __name__ == "__main__":
    df = load_data('data.csv')
    plot_data(df, 'column1')
```

### Enhanced Implementation
```python
def plot_data(data, column_name):
    """Plot a histogram with error handling for column existence."""
    if column_name not in data.columns:
        raise ValueError(f"Column {column_name} does not exist for plotting.")
    
    plt.hist(data[column_name], bins=10)
    plt.title(f'Histogram of {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.show()

# Example usage
if __name__ == "__main__":
    try:
        df = load_data('data.csv')
        plot_data(df, 'column1')
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Testing the Solution
```python
def test_plot_data():
    """Test the plot_data function with various cases."""
    df = pd.DataFrame({
        'column1': [1,