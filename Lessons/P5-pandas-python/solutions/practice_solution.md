---
title: introduction to pandas python - Practice Solution
layout: layouts/course.njk
courseId: P5-pandas-python
tags:
  - solutions
  - code
date: 2025-12-08T17:03:38.981168
---
# Introduction to Pandas in Python: Practice Solutions

This document serves as a comprehensive guide to practicing and mastering the key concepts of the Pandas library in Python. It is structured to provide a foundational understanding through hands-on exercises, culminating in real-world project implementations.

## Learning Objectives
- Master key concepts of Pandas
- Apply practical techniques for data manipulation and analysis
- Build real-world projects using the Pandas library

---

## Exercise 1: DataFrame Creation and Basic Operations

### Overview
In this exercise, we will create a Pandas DataFrame from a dictionary and demonstrate basic operations like viewing, accessing, and manipulating data.

### Basic Implementation
```python
import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Initializing the DataFrame
df = pd.DataFrame(data)

# Displaying the DataFrame
print("Initial DataFrame:")
print(df)

# Accessing a specific column
print("\nNames in the DataFrame:")
print(df['Name'])

# Adding a new column
df['Salary'] = [70000, 80000, 90000]
print("\nDataFrame after adding Salary:")
print(df)
```

### Enhanced Implementation
```python
import pandas as pd

def create_dataframe(data):
    """
    Create a DataFrame from the given dictionary data.
    
    Parameters:
        data (dict): A dictionary containing data for the DataFrame.
        
    Returns:
        DataFrame: A Pandas DataFrame created from the data.
    """
    try:
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        print(f"Error creating DataFrame: {e}")
        return None

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Creating the DataFrame
df = create_dataframe(data)

if df is not None:
    print("Initial DataFrame:")
    print(df)

    # Accessing a specific column with error handling
    try:
        print("\nNames in the DataFrame:")
        print(df['Name'])
    except KeyError as e:
        print(f"Column not found: {e}")

    # Adding a new column with validation
    try:
        df['Salary'] = [70000, 80000, 90000]
        print("\nDataFrame after adding Salary:")
        print(df)
    except Exception as e:
        print(f"Error adding Salary column: {e}")
```

### Testing the Solution
```python
def test_create_dataframe():
    test_data = {
        'Name': ['Dave', 'Eve'],
        'Age': [28, 22],
        'City': ['Miami', 'Seattle']
    }
    
    df = create_dataframe(test_data)
    assert df is not None, "DataFrame should not be None"
    assert df.shape == (2, 3), "DataFrame should have 2 rows and 3 columns"
    assert 'Name' in df.columns, "Name column should exist"

# Run the test
test_create_dataframe()
print("All tests passed!")
```

### Explanation
- **Design Decisions**: The choice to encapsulate DataFrame creation in a function allows for easy reuse and better error management. 
- **Key Concepts**: The exercise demonstrates how to create DataFrames, access columns, and manipulate data.
- **Complexity Analysis**: The time complexity for creating a DataFrame is O(n) where n is the number of rows.

### Key Takeaways
- Always validate data before processing.
- Use try-except blocks to handle potential errors gracefully.
- Structuring code into functions promotes reusability and testing.

---

## Exercise 2: DataFrame Filtering and Grouping

### Overview
This exercise involves filtering a DataFrame based on certain conditions and grouping data.

### Basic Implementation
```python
import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Score': [85, 90, 78, 92, 88],
    'City': ['New York', 'New York', 'Chicago', 'Chicago', 'Los Angeles']
}

df = pd.DataFrame(data)

# Filtering DataFrame for scores greater than 80
filtered_df = df[df['Score'] > 80]
print("Filtered DataFrame (Scores > 80):")
print(filtered_df)

# Grouping by City and calculating average score
grouped_df = df.groupby('City')['Score'].mean().reset_index()
print("\nAverage Scores by City:")
print(grouped_df)
```

### Enhanced Implementation
```python
import pandas as pd

def filter_scores(df, threshold):
    """
    Filter the DataFrame for scores above the given threshold.
    
    Parameters:
        df (DataFrame): The DataFrame to filter.
        threshold (int): The score threshold for filtering.
        
    Returns:
        DataFrame: A DataFrame containing scores above the threshold.
    """
    try:
        return df[df['Score'] > threshold]
    except KeyError as e:
        print(f"Column not found: {e}")
        return None

def average_scores_by_city(df):
    """
    Group the DataFrame by City and calculate the average score.
    
    Parameters:
        df (DataFrame): The DataFrame to group.
        
    Returns:
        DataFrame: A DataFrame containing average scores by city.
    """
    try:
        return df.groupby('City')['Score'].mean().reset_index()
    except Exception as e:
        print(f"Error during grouping: {e}")
        return None

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Score': [85, 90, 78, 92, 88],
    'City': ['New York', 'New York', 'Chicago', 'Chicago', 'Los Angeles']
}

df = pd.DataFrame(data)

# Filtering scores
filtered_df = filter_scores(df, 80)
if filtered_df is not None:
    print("Filtered DataFrame (Scores > 80):")
    print(filtered_df)

# Grouping by city
grouped_df = average_scores_by_city(df)
if grouped_df is not None:
    print("\nAverage Scores by City:")
    print(grouped_df)
```

### Testing the Solution
```python
def test_filter_scores():
    test_data = {
        'Name': ['Alice', 'Bob'],
        'Score': [85, 75],
        'City': ['New York', 'Los Angeles']
    }
    df = pd.DataFrame(test_data)
    result = filter_scores(df, 80)
    assert result.shape[0] == 1, "Should only return one row for scores > 80"
    assert result.iloc[0]['Name'] == 'Alice', "Should return Alice"

def test_average_scores_by_city():
    test_data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Score': [90, 80, 70],
        'City': ['New York', 'New York', 'Los Angeles']
    }
    df = pd.DataFrame(test_data)
    result = average_scores_by_city(df)
    assert result.shape[0] == 2, "Should return average for two cities"
    assert result[result['City'] == 'New York']['Score'].values[0] == 85, "Average score for New York should be 85"

# Run tests
test_filter_scores()
test_average_scores_by_city()
print("All tests passed!")
```

### Explanation
- **Design Decisions**: Functions for filtering and grouping make the code modular and easier to maintain.
- **Key Concepts**: Filtering allows us to extract relevant data, while grouping helps summarize information efficiently.
- **Complexity Analysis**: Filtering operation runs in O(n), while grouping runs in O(n log n) due to sorting.

### Key Takeaways
- Effective data analysis often involves filtering and grouping.
- Always include error handling to manage potential issues with data.
- Testing ensures that functions behave as expected and helps catch errors early.

---

This document provides a structured approach to learning and applying the Pandas library through hands-on exercises. By following these examples, one can build a solid foundation in data manipulation and analysis with Python.