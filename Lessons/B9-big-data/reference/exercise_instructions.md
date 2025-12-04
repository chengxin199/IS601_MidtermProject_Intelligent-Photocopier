---
title: Introduction to big data - Exercise Instructions
layout: layouts/course.njk
courseId: B9-big-data
tags:
  - exercises
  - practice
date: 2025-12-04T15:34:40.959971
---
## Exercise 1: Reading and Summarizing Large CSV Files
**Difficulty:** Beginner  
**Time Estimate:** 20 minutes

### Objective
Implement a function to efficiently read a large CSV file in chunks and compute summary statistics (mean, median, mode) for a numeric column without loading the entire file into memory.

### Starter Code
```python
import pandas as pd

def summarize_large_csv(file_path, column_name, chunk_size=10000):
    """
    Reads a large CSV file in chunks and computes mean, median, and mode for a specified numeric column.
    
    Args:
        file_path (str): Path to the CSV file.
        column_name (str): Name of the numeric column to summarize.
        chunk_size (int): Number of rows per chunk to process.
        
    Returns:
        dict: Dictionary with keys 'mean', 'median', 'mode' and their computed values.
    """
    # TODO: Implement reading the CSV in chunks and aggregate results
    pass
```

### Requirements
- Use pandas `read_csv` with `chunksize` to process the file in parts.
- Compute mean, median, and mode incrementally or aggregate partial results.
- Handle missing or non-numeric values gracefully (ignore them).
- Return results as a dictionary with keys `'mean'`, `'median'`, and `'mode'`.

### Test Cases
```python
# Create a sample CSV file for testing
import pandas as pd

df = pd.DataFrame({
    'id': range(1, 11),
    'value': [10, 20, 20, 30, 40, None, 20, 10, 30, 40]
})
df.to_csv('test.csv', index=False)

result = summarize_large_csv('test.csv', 'value', chunk_size=3)
# mean = (10+20+20+30+40+20+10+30+40)/9 = 24.44 approx (None excluded)
# median = 20
# mode = 20
assert abs(result['mean'] - 24.44) < 0.01
assert result['median'] == 20
assert result['mode'] == 20
```

### Hints
- Use `pd.read_csv(..., chunksize=chunk_size)` to read data in parts.
- For mean, keep track of sum and count as you iterate.
- For median and mode, consider collecting values in a list if memory permits or use approximate methods.
- Use `pd.Series.mode()` to find mode for each chunk.


---

## Exercise 2: Word Frequency Count from Large Text Files
**Difficulty:** Intermediate  
**Time Estimate:** 30 minutes

### Objective
Implement a function to process a very large text file line by line and compute the frequency of each word, ignoring case and punctuation.

### Starter Code
```python
import string
from collections import defaultdict

def word_frequency_large_file(file_path):
    """
    Reads a large text file line by line and counts the frequency of each word.
    
    Args:
        file_path (str): Path to the text file.
        
    Returns:
        dict: Dictionary mapping words to their frequency counts.
    """
    word_counts = defaultdict(int)
    # TODO: Open file and process line by line
    # Normalize words (lowercase, strip punctuation)
    pass
```

### Requirements
- Process the file line-by-line without loading the whole file into memory.
- Normalize words by converting to lowercase and removing punctuation.
- Update counts in a dictionary or defaultdict.
- Return the frequency dictionary.
- Handle empty lines or lines with no words gracefully.

### Test Cases
```python
with open('test_text.txt', 'w') as f:
    f.write("Hello world!\n")
    f.write("Hello, HELLO? World...\n")
    f.write("\n")
    f.write("Big data is big.\n")

freq = word_frequency_large_file('test_text.txt')
assert freq['hello'] == 3
assert freq['world'] == 2
assert freq['big'] == 2
assert freq['data'] == 1
assert freq.get('is', 0) == 1
```

### Hints
- Use `str.translate` with `str.maketrans` to remove punctuation efficiently.
- Use a `with open(file_path, 'r') as f:` block and iterate lines.
- Split lines on whitespace with `line.split()`.
- Remember to strip newline characters.


---

## Exercise 3: Implementing a Simple MapReduce Word Count
**Difficulty:** Intermediate  
**Time Estimate:** 40 minutes

### Objective
Simulate a simple MapReduce-style word count by splitting a text dataset into chunks, mapping words to counts, and then reducing (aggregating) counts across chunks.

### Starter Code
```python
from collections import Counter
import math

def map_word_count(lines):
    """
    Map function: counts words in a list of lines.
    
    Args:
        lines (list of str): Lines of text.
        
    Returns:
        Counter: Word counts in these lines.
    """
    # TODO: Implement counting words in lines
    pass

def reduce_word_counts(counters):
    """
    Reduce function: aggregates a list of Counters into one Counter.
    
    Args:
        counters (list of Counter): List of word count Counters.
        
    Returns:
        Counter: Aggregated word counts.
    """
    # TODO: Implement aggregation of counters
    pass

def mapreduce_word_count(file_path, chunk_size=1000):
    """
    Reads file in chunks, applies map and reduce to get word counts.
    
    Args:
        file_path (str): Path to text file.
        chunk_size (int): Number of lines per chunk.
        
    Returns:
        dict: Word count dictionary.
    """
    counters = []
    # TODO: Read file by chunks, apply map, collect results
    # Then reduce all counters into one
    pass
```

### Requirements
- `map_word_count`: normalize words (lowercase, remove punctuation) and count frequencies in input lines.
- `reduce_word_counts`: combine multiple Counters into one by summing counts.
- `mapreduce_word_count`: read the file line-by-line, group lines into chunks of `chunk_size`, map each chunk, then reduce all.
- Return the final aggregated word counts as a dictionary.

### Test Cases
```python
with open('test_text2.txt', 'w') as f:
    f.write("Big data and big challenges.\n")
    f.write("Data is the new oil.\n")
    f.write("Challenges in big data.\n")

result = mapreduce_word_count('test_text2.txt', chunk_size=2)
assert result['big'] == 3
assert result['data'] == 3
assert result['challenges'] == 2
assert result['and'] == 1
assert result['is'] == 1
assert result['the'] == 1
assert result['new'] == 1
assert result['oil'] == 1
```

### Hints
- Use `Counter.update()` to accumulate counts.
- Use `str.maketrans` to remove punctuation.
- Group lines into chunks using a simple loop and slicing or a temporary list.
- Remember to process the last chunk if it has fewer lines than `chunk_size`.

---

## Exercise 4: Aggregating Streaming Data with Sliding Window
**Difficulty:** Advanced  
**Time Estimate:** 45 minutes

### Objective
Build a function to process a simulated data stream of numeric values and compute a sliding window average of the last N values at each step.

### Starter Code
```python
from collections import deque

def sliding_window_average(stream, window_size):
    """
    Given an iterable stream of numbers, compute the sliding window average of size window_size.
    
    Args:
        stream (iterable): Stream of numeric values.
        window_size (int): Size of the sliding window.
        
    Returns:
        list: List of averages after each new value is processed.
    """
    window = deque()
    averages = []
    current_sum = 0
    # TODO: Implement sliding window average logic
    pass
```

### Requirements
- Use a deque to maintain the current window of values for O(1) insertion/removal.
- Update sum incrementally to avoid recomputing sums.
- For each new value from the stream, add it to the window, remove oldest if needed.
- Append the current average to the output list.
- Handle streams shorter than window size gracefully.

### Test Cases
```python
stream = [10, 20, 30, 40, 50]
result = sliding_window_average(stream, 3)
# windows: [10], avg=10; [10,20], avg=15; [10,20,30], avg=20; [20,30,40], avg=30; [30,40,50], avg=40
expected = [10, 15, 20, 30, 40]
assert result == expected

stream2 = [5]
result2 = sliding_window_average(stream2, 3)
assert result2 == [5]
```

### Hints
- Use `deque.append()` to add and `deque.popleft()` to remove oldest.
- Keep track of `current_sum` by adding new values and subtracting removed values.
- The average at each step is `current_sum / len(window)`.

---

## Exercise 5: Simple Data Partitioning for Parallel Processing
**Difficulty:** Advanced  
**Time Estimate:** 40 minutes

### Objective
Write a function to partition a large list of data into N approximately equal chunks for parallel processing. Then implement a function to process each chunk independently and combine the results.

### Starter Code
```python
def partition_data(data, num_partitions):
    """
    Partition data into num_partitions roughly equal chunks.
    
    Args:
        data (list): List of data items.
        num_partitions (int): Number of partitions.
        
    Returns:
        list of lists: List containing data chunks.
    """
    # TODO: Implement partitioning logic
    pass

def process_partitions(partitions, func):
    """
    Process each data partition with a given function and combine results.
    
    Args:
        partitions (list of lists): Data partitions.
        func (callable): Function to apply to each partition.
        
    Returns:
        list: Combined results from each partition.
    """
    # TODO: Apply func to each partition and combine results
    pass
```

### Requirements
- Partition the input list into `num_partitions` sublists with sizes differing by at most 1.
- `process_partitions` applies the function `func` on each sublist and collects results in a single list.
- Example use case: partition a list of numbers, square each number in partitions, and combine results.
- Handle edge case where `num_partitions` > length of data.

### Test Cases
```python
data = [1, 2, 3, 4, 5, 6, 7]
partitions = partition_data(data, 3)
# partitions could be [[1,2,3],[4,5],[6,7]] or similar
assert sum(len(p) for p in partitions) == len(data)
assert abs(len(partitions[0]) - len(partitions[1])) <= 1

def square_list(lst):
    return [x*x for x in lst]

result = process_partitions(partitions, square_list)
assert sorted(result) == sorted([1,4,9,16,25,36,49])
```

### Hints
- Use integer division and modulo to determine base partition size and distribute remainder.
- Loop through data and slice accordingly.
- Use list comprehension or a simple loop to apply `func` on each partition.
- Flatten results with list concatenation or `itertools.chain`.