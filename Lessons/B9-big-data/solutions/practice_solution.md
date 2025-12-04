---
title: Introduction to big data - Practice Solution
layout: layouts/course.njk
courseId: B9-big-data
tags:
  - solutions
  - code
date: 2025-12-04T15:35:29.396390
---
# Introduction to Big Data: Practice Solution Document

---

## Exercise 1: Reading and Processing Large CSV Files Efficiently

### Overview
In big data, efficiently processing large CSV files without loading everything into memory is essential. We'll demonstrate how to read and process large CSVs line-by-line (streaming) to master key concepts of memory-efficient data handling.

---

### Basic Implementation

```python
import csv

def count_rows_basic(file_path):
    """
    Counts the number of rows in a CSV file by iterating line-by-line.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        int: Number of rows in the CSV file.
    """
    row_count = 0
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for _ in reader:
            row_count += 1  # Increment row count for each row
    return row_count
```

---

### Enhanced Implementation

```python
import csv
import os

def count_rows_enhanced(file_path):
    """
    Counts the number of rows in a CSV file with error handling.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        int: Number of rows in the CSV file.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the file cannot be accessed due to permission.
        ValueError: If the file is empty or not a valid CSV.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if not os.path.isfile(file_path):
        raise ValueError(f"Path is not a file: {file_path}")

    row_count = 0

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                row_count += 1
    except csv.Error as e:
        raise ValueError(f"CSV parsing error: {e}")

    if row_count == 0:
        raise ValueError("CSV file is empty")

    return row_count
```

---

### Testing the Solution

```python
import tempfile
import os

def test_count_rows_basic():
    # Create a temporary CSV file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, newline='', encoding='utf-8') as tmp:
        tmp.write("id,name,age\n1,Alice,30\n2,Bob,25\n3,Charlie,35\n")
        tmp_path = tmp.name

    try:
        assert count_rows_basic(tmp_path) == 4  # Header + 3 rows
        print("Basic count_rows test passed.")
    finally:
        os.remove(tmp_path)

def test_count_rows_enhanced():
    with tempfile.NamedTemporaryFile(mode='w', delete=False, newline='', encoding='utf-8') as tmp:
        tmp.write("id,name\n1,Alice\n2,Bob\n")
        tmp_path = tmp.name

    try:
        assert count_rows_enhanced(tmp_path) == 3  # Header + 2 rows
        print("Enhanced count_rows test passed.")
    finally:
        os.remove(tmp_path)

def test_count_rows_enhanced_errors():
    try:
        count_rows_enhanced("non_existent_file.csv")
    except FileNotFoundError:
        print("FileNotFoundError correctly raised.")

    # Create an empty file to test empty CSV
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
        tmp_path = tmp.name

    try:
        count_rows_enhanced(tmp_path)
    except ValueError as e:
        assert str(e) == "CSV file is empty"
        print("Empty CSV file error correctly raised.")
    finally:
        os.remove(tmp_path)

if __name__ == "__main__":
    test_count_rows_basic()
    test_count_rows_enhanced()
    test_count_rows_enhanced_errors()
```

---

### Explanation

- **Design Decisions:**
  - Use Python’s built-in `csv` module to handle CSV parsing reliably.
  - Process the file line-by-line to keep memory footprint low, crucial for big data.
  - Enhanced version includes file existence and type checks, and CSV parsing error handling.
- **Key Concepts:**
  - Streaming data processing.
  - Defensive programming with error handling.
- **Complexity:**
  - Time: O(n), where n = number of rows.
  - Space: O(1), constant memory usage regardless of file size.

---

### Key Takeaways

- Avoid loading large files entirely into memory when possible.
- Always add error handling to manage file-related exceptions.
- Use built-in libraries optimized for parsing common data formats.
- Testing edge cases (empty files, missing files) is critical for robustness.

---

## Exercise 2: Counting Word Frequencies in a Large Text File

### Overview
Counting word frequencies is a common big data task for text analysis. This exercise shows how to process large text files efficiently and build a frequency distribution.

---

### Basic Implementation

```python
from collections import Counter
import re

def count_word_frequencies_basic(file_path):
    """
    Counts word frequencies in a text file.

    Args:
        file_path (str): Path to the text file.

    Returns:
        Counter: Dictionary-like object with word counts.
    """
    word_freq = Counter()
    with open(file_path, mode='r', encoding='utf-8') as f:
        for line in f:
            # Extract words ignoring punctuation, convert to lowercase
            words = re.findall(r'\b\w+\b', line.lower())
            word_freq.update(words)
    return word_freq
```

---

### Enhanced Implementation

```python
from collections import Counter
import re
import os

def count_word_frequencies_enhanced(file_path):
    """
    Counts word frequencies in a text file with error handling.

    Args:
        file_path (str): Path to the text file.

    Returns:
        Counter: Dictionary-like object with word counts.

    Raises:
        FileNotFoundError: If file does not exist.
        PermissionError: If file cannot be accessed.
        ValueError: If file is empty.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    word_freq = Counter()
    total_words = 0

    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            for line in f:
                words = re.findall(r'\b\w+\b', line.lower())
                word_freq.update(words)
                total_words += len(words)
    except Exception as e:
        raise ValueError(f"Error reading file: {e}")

    if total_words == 0:
        raise ValueError("The file contains no words.")

    return word_freq
```

---

### Testing the Solution

```python
import tempfile
import os

def test_count_word_frequencies_basic():
    text = "Hello world! Hello, Big Data.\nBig data is fun."
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as tmp:
        tmp.write(text)
        tmp_path = tmp.name

    try:
        freq = count_word_frequencies_basic(tmp_path)
        assert freq['hello'] == 2
        assert freq['big'] == 2
        assert freq['data'] == 2
        assert freq['world'] == 1
        assert freq['is'] == 1
        assert freq['fun'] == 1
        print("Basic word frequency test passed.")
    finally:
        os.remove(tmp_path)

def test_count_word_frequencies_enhanced():
    text = "Big data is big."
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as tmp:
        tmp.write(text)
        tmp_path = tmp.name

    try:
        freq = count_word_frequencies_enhanced(tmp_path)
        assert freq['big'] == 2
        assert freq['data'] == 1
        assert freq['is'] == 1
        print("Enhanced word frequency test passed.")
    finally:
        os.remove(tmp_path)

def test_count_word_frequencies_enhanced_errors():
    try:
        count_word_frequencies_enhanced("missing.txt")
    except FileNotFoundError:
        print("FileNotFoundError correctly raised.")

    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as tmp:
        tmp_path = tmp.name  # Empty file

    try:
        count_word_frequencies_enhanced(tmp_path)
    except ValueError as e:
        assert str(e) == "The file contains no words."
        print("Empty file error correctly raised.")
    finally:
        os.remove(tmp_path)

if __name__ == "__main__":
    test_count_word_frequencies_basic()
    test_count_word_frequencies_enhanced()
    test_count_word_frequencies_enhanced_errors()
```

---

### Explanation

- **Design Decisions:**
  - Use `re.findall` to normalize and extract words, removing punctuation.
  - Use `Counter` for efficient counting.
  - Enhanced version checks for file existence, permissions, and empty file.
- **Key Concepts:**
  - Text normalization and tokenization.
  - Frequency distribution.
- **Complexity:**
  - Time: O(n) where n = number of words.
  - Space: O(m) where m = number of unique words.

---

### Key Takeaways

- Normalize text to lowercase for consistent counting.
- Use regular expressions to tokenize words.
- `collections.Counter` is ideal for frequency counts.
- Validate inputs and handle empty or missing files gracefully.

---

## Exercise 3: Aggregating Data Using MapReduce Paradigm (Simulated)

### Overview
MapReduce is a core technique in big data for parallel data processing. We simulate a simple MapReduce word count on a list of text chunks, illustrating distributed processing concepts.

---

### Basic Implementation

```python
from collections import Counter

def map_function(text_chunk):
    """
    Map function that counts word frequencies in a text chunk.

    Args:
        text_chunk (str): Text data chunk.

    Returns:
        Counter: Word frequency counts in the chunk.
    """
    words = text_chunk.lower().split()
    return Counter(words)

def reduce_function(counters):
    """
    Reduce function that aggregates multiple Counters.

    Args:
        counters (list of Counter): List of counters to aggregate.

    Returns:
        Counter: Aggregated word counts.
    """
    total_counter = Counter()
    for counter in counters:
        total_counter.update(counter)
    return total_counter

def mapreduce_word_count(text_chunks):
    """
    Simulates MapReduce to count words from multiple text chunks.

    Args:
        text_chunks (list of str): List of text chunks.

    Returns:
        Counter: Aggregated word counts.
    """
    mapped = [map_function(chunk) for chunk in text_chunks]
    reduced = reduce_function(mapped)
    return reduced
```

---

### Enhanced Implementation

```python
from collections import Counter
import re

def map_function_enhanced(text_chunk):
    """
    Map function to count word frequencies with normalization and error handling.

    Args:
        text_chunk (str): Text data chunk.

    Returns:
        Counter: Word frequency counts in the chunk.

    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(text_chunk, str):
        raise TypeError("Text chunk must be a string")

    # Use regex to extract words, make lowercase
    words = re.findall(r'\b\w+\b', text_chunk.lower())
    return Counter(words)

def reduce_function_enhanced(counters):
    """
    Reduce function that aggregates multiple Counters with validation.

    Args:
        counters (list of Counter): List of counters to aggregate.

    Returns:
        Counter: Aggregated word counts.

    Raises:
        TypeError: If input is not a list of Counters.
    """
    if not isinstance(counters, list):
        raise TypeError("Input must be a list")

    total_counter = Counter()
    for c in counters:
        if not isinstance(c, Counter):
            raise TypeError("All elements must be Counter instances")
        total_counter.update(c)

    return total_counter

def mapreduce_word_count_enhanced(text_chunks):
    """
    Simulates MapReduce word count with input validation.

    Args:
        text_chunks (list of str): List of text chunks.

    Returns:
        Counter: Aggregated word counts.

    Raises:
        TypeError: If input is not a list of strings.
    """
    if not isinstance(text_chunks, list):
        raise TypeError("Input must be a list")

    for chunk in text_chunks:
        if not isinstance(chunk, str):
            raise TypeError("All text chunks must be strings")

    mapped = [map_function_enhanced(chunk) for chunk in text_chunks]
    reduced = reduce_function_enhanced(mapped)
    return reduced
```

---

### Testing the Solution

```python
def test_mapreduce_basic():
    chunks = [
        "Big data is big",
        "Data science is cool",
        "Big data analysis"
    ]
    result = mapreduce_word_count(chunks)
    assert result['big'] == 3
    assert result['data'] == 3
    assert result['is'] == 2
    assert result['science'] == 1
    assert result['cool'] == 1
    assert result['analysis'] == 1
    print("Basic MapReduce test passed.")

def test_mapreduce_enhanced():
    chunks = [
        "Big data, big data!",
        "Data science is cool.",
        "Big data analysis."
    ]
    result = mapreduce_word_count_enhanced(chunks)
    assert result['big'] == 3
    assert result['data'] == 4  # Note: punctuation stripped, counts increased
    assert result['is'] == 1
    assert result['science'] == 1
    assert result['cool'] == 1
    assert result['analysis'] == 1
    print("Enhanced MapReduce test passed.")

def test_mapreduce_enhanced_errors():
    try:
        mapreduce_word_count_enhanced("not a list")
    except TypeError:
        print("TypeError correctly raised for non-list input.")

    try:
        mapreduce_word_count_enhanced([123, "valid string"])
    except TypeError:
        print("TypeError correctly raised for non-string chunk.")

if __name__ == "__main__":
    test_mapreduce_basic()
    test_mapreduce_enhanced()
    test_mapreduce_enhanced_errors()
```

---

### Explanation

- **Design Decisions:**
  - Simulate distributed MapReduce by splitting data into chunks (map phase) and aggregating results (reduce phase).
  - Use regex in enhanced to handle punctuation and normalization.
  - Add input validation to ensure robustness.
- **Key Concepts:**
  - MapReduce programming model: map (process chunks), reduce (aggregate results).
  - Importance of normalization in text processing.
- **Complexity:**
  - Time: O(n), n = total words across all chunks.
  - Space: O(m), m = unique words.

---

### Key Takeaways

- MapReduce abstracts parallel data processing into map and reduce stages.
- Preprocessing (normalization, tokenization) is critical for consistent results.
- Input validation improves code robustness.
- This pattern scales well in distributed big data environments.

---

# Summary

This document provided three comprehensive, production-quality practice solutions for introductory big data concepts:

- Efficient file reading with streaming.
- Text processing for word frequency analysis.
- Simulated MapReduce for distributed aggregation.

Each solution includes:

- Basic and enhanced implementations.
- Detailed inline comments.
- Thorough test cases.
- Alternative approaches and explanations.

These exercises build strong foundations for mastering big data processing techniques in real-world scenarios.