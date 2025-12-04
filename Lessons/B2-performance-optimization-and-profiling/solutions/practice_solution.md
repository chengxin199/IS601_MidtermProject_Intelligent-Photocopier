---
title: Performance Optimization and Profiling - Practice Solution
layout: layouts/course.njk
courseId: B2-performance-optimization-and-profiling
tags:
  - solutions
  - code
date: 2025-11-17T19:47:07.408565
---
# Practice Solution - Performance Optimization and Profiling

## Overview
This document provides a comprehensive approach to performance optimization and profiling in Python applications. We will begin by identifying bottlenecks using profiling tools, followed by practical optimization techniques such as algorithm improvements, data structure choices, memory management, caching, and concurrency patterns. Each solution example will build upon the previous one, demonstrating progressive levels of optimization and best practices including error handling and validation of performance gains.

---

## Solution 1: Basic Implementation - Profiling and Simple Optimization

```python
import cProfile
import pstats
import io

def inefficient_sum(n):
    """Inefficiently sums numbers from 0 to n-1 using a loop and list."""
    total = 0
    nums = []
    for i in range(n):
        nums.append(i)
    for num in nums:
        total += num
    return total

def main():
    result = inefficient_sum(10**6)
    print(f"Sum result: {result}")

if __name__ == "__main__":
    # Profile the main function and output stats
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()

    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream).sort_stats('cumulative')
    stats.print_stats(10)  # print top 10 functions
    print(stream.getvalue())
```

### Explanation:
- We use `cProfile` to identify performance bottlenecks.
- The function `inefficient_sum` builds a list before summing, which is unnecessary.
- Profiling output will show time spent inside the loops and list operations.

---

## Solution 2: Enhanced Implementation - Algorithm and Data Structure Optimization

```python
def optimized_sum(n):
    """Sum numbers from 0 to n-1 using built-in sum and range for efficiency."""
    try:
        # Using built-in sum and range is faster and memory efficient
        return sum(range(n))
    except TypeError:
        print("Input must be an integer")
        return None

def main():
    n = 10**6
    result = optimized_sum(n)
    if result is not None:
        print(f"Optimized sum result: {result}")

if __name__ == "__main__":
    main()
```

### Explanation:
- Replaced manual list appending and looping with Python’s optimized `sum(range(n))`.
- Reduces memory usage and improves speed.
- Added basic error handling to check input type.

---

## Solution 3: Advanced Implementation - Caching with Memoization and Parallel Processing

```python
from functools import lru_cache
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

@lru_cache(maxsize=128)
def fibonacci(n):
    """Compute Fibonacci numbers using memoization to avoid redundant calculations."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def compute_fibonacci_numbers(numbers):
    """Compute Fibonacci numbers in parallel using ThreadPoolExecutor."""
    results = {}
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Submit tasks
        future_to_num = {executor.submit(fibonacci, num): num for num in numbers}
        for future in as_completed(future_to_num):
            num = future_to_num[future]
            try:
                results[num] = future.result()
            except Exception as e:
                print(f"Error computing fibonacci({num}): {e}")
    return results

def main():
    numbers = [35, 36, 37, 38]  # Expensive Fibonacci numbers
    start_time = time.time()
    fib_results = compute_fibonacci_numbers(numbers)
    end_time = time.time()

    for num in numbers:
        print(f"Fibonacci({num}) = {fib_results[num]}")

    print(f"Computed in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
```

### Explanation:
- Uses `functools.lru_cache` to memoize Fibonacci results, avoiding repeated expensive calls.
- Leverages `ThreadPoolExecutor` to compute multiple Fibonacci numbers in parallel.
- Includes error handling for invalid input and exceptions during task execution.
- Measures execution time to validate performance improvements.

---

## Explanation

### Profiling to Identify Bottlenecks
- Using `cProfile` allows pinpointing which functions consume the most time.
- In Solution 1, we identified inefficient list creation and looping as bottlenecks.

### Algorithmic and Data Structure Optimization
- Replacing loops and manual list management with built-in functions (`sum(range(n))`) yields significant speed-ups and reduces memory overhead.
- Proper error handling ensures robustness.

### Memory Management and Garbage Collection
- Using generators or built-in iterators reduces peak memory usage.
- The `lru_cache` decorator caches results to prevent redundant calculations, effectively trading memory for speed.

### Caching and Memoization
- Memoization dramatically improves performance in recursive computations like Fibonacci.
- Setting a sensible `maxsize` for the cache balances memory usage.

### Parallel Processing
- Python's `concurrent.futures.ThreadPoolExecutor` allows concurrent execution of independent tasks, ideal for I/O-bound or CPU-bound tasks when combined with memoization.
- Proper error handling within threads prevents silent failures.

### Measuring and Validating Performance
- Timing code sections (using `time.time()` or more precise `time.perf_counter()`) before and after optimization helps quantify improvements.
- Profiling after optimization ensures bottlenecks are resolved.

---

## Key Takeaways
- **Profiling is essential**: Always profile your code before optimizing to focus on real bottlenecks.
- **Leverage built-in functions and data structures** for efficient, readable code.
- **Use memoization and caching** to avoid redundant computations, especially for recursive or repeated calls.
- **Apply parallelism prudently**: Use threading or multiprocessing to speed up independent tasks, but be mindful of Python’s GIL and task nature.
- **Manage memory wisely**: Use generators and limit cache sizes to avoid excessive memory usage.
- **Measure performance improvements** quantitatively to validate optimization efforts.
- **Incorporate error handling** to build robust and maintainable optimized code.

By following these steps and best practices, you can systematically optimize Python applications while maintaining code clarity and reliability.