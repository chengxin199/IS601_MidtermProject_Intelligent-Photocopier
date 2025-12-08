---
title: introduction to big data - Exercise Instructions
layout: layouts/course.njk
courseId: B9-big-data
tags:
  - exercises
  - practice
date: 2025-12-08T16:00:23.094189
---
## Exercise 1: Introduction to Data Loading
**Difficulty:** Beginner  
**Time Estimate:** 30 minutes  

### Objective
In this exercise, you will implement a function to load a CSV file into a pandas DataFrame. You will also explore basic data inspection techniques.

### Starter Code
```python
import pandas as pd

def load_data(file_path):
    # TODO: Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)
    return df
```

### Requirements
- Use the `pandas` library to read the CSV file.
- Return the loaded DataFrame.
- Handle the case where the file does not exist by returning `None`.

### Test Cases
```python
# Example test cases
df = load_data('data/sample_data.csv')
assert df is not None  # Check if DataFrame is loaded
assert isinstance(df, pd.DataFrame)  # Check if it's a DataFrame
```

### Hints
- Use `try...except` to handle file loading errors.
- Print the DataFrame's head to inspect the first few rows after loading.

---

## Exercise 2: Data Exploration
**Difficulty:** Beginner  
**Time Estimate:** 45 minutes  

### Objective
You will implement functions to perform basic data exploration tasks, such as checking the shape of the DataFrame and displaying summary statistics.

### Starter Code
```python
def explore_data(df):
    # TODO: Implement the exploration of the DataFrame
    shape = df.shape
    summary = df.describe()
    return shape, summary
```

### Requirements
- Return the shape of the DataFrame as a tuple (rows, columns).
- Return summary statistics of the numerical columns.
- Handle the case where the DataFrame is empty.

### Test Cases
```python
# Example test cases
df = load_data('data/sample_data.csv')
shape, summary = explore_data(df)
assert shape == (100, 5)  # Example expected shape
assert 'mean' in summary.columns  # Check if summary has mean
```

### Hints
- Use `df.shape` to get the dimensions.
- Use `df.describe()` for statistical summaries.

---

## Exercise 3: Data Cleaning
**Difficulty:** Intermediate  
**Time Estimate:** 60 minutes  

### Objective
You will implement a function to clean the DataFrame by handling missing values and removing duplicates.

### Starter Code
```python
def clean_data(df):
    # TODO: Clean the DataFrame by removing duplicates and filling missing values
    df = df.drop_duplicates()
    df.fillna(0, inplace=True)  # Example: fill missing values with 0
    return df
```

### Requirements
- Remove duplicate rows.
- Fill missing values with a specified method (e.g., mean, median, or a constant).
- Return the cleaned DataFrame.

### Test Cases
```python
# Example test cases
df = load_data('data/sample_data_with_nan.csv')
cleaned_df = clean_data(df)
assert cleaned_df.isnull().sum().sum() == 0  # Check for no NaN values
assert cleaned_df.duplicated().sum() == 0  # Check for no duplicates
```

### Hints
- Use `df.drop_duplicates()` to remove duplicates.
- Use `df.fillna()` to handle missing values.

---

## Exercise 4: Basic Visualization
**Difficulty:** Intermediate  
**Time Estimate:** 45 minutes  

### Objective
You will implement a function that creates a simple bar plot using `matplotlib` to visualize categorical data.

### Starter Code
```python
import matplotlib.pyplot as plt

def plot_data(df, column):
    # TODO: Create a bar plot for the specified column
    counts = df[column].value_counts()
    counts.plot(kind='bar')
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Counts')
    plt.show()
```

### Requirements
- Create a bar plot showing the distribution of a specified categorical column.
- Ensure the plot displays labels and a title.

### Test Cases
```python
# Example test cases
df = load_data('data/sample_data.csv')
plot_data(df, 'category_column')  # This should display a plot
```

### Hints
- Use `value_counts()` to get counts of unique values in a column.
- Make sure you have `matplotlib` installed and imported.

---

## Exercise 5: Data Exporting
**Difficulty:** Intermediate  
**Time Estimate:** 30 minutes  

### Objective
In this exercise, you will implement a function to save the cleaned DataFrame back to a new CSV file.

### Starter Code
```python
def save_data(df, output_file):
    # TODO: Save the DataFrame to a CSV file
    df.to_csv(output_file, index=False)
```

### Requirements
- Save the DataFrame to a specified CSV file.
- Ensure that the index is not included in the output file.

### Test Cases
```python
# Example test cases
df = load_data('data/sample_data.csv')
cleaned_df = clean_data(df)
save_data(cleaned_df, 'data/cleaned_data.csv')
assert os.path.exists('data/cleaned_data.csv')  # Check if file is created
```

### Hints
- Use `df.to_csv()` to save the DataFrame.
- Ensure the file path is correct when saving the file.