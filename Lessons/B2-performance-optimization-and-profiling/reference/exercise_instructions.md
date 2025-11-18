---
title: Performance Optimization and Profiling - Exercise Instructions
layout: layouts/base.njk
courseId: B2-performance-optimization-and-profiling
tags:
  - exercises
  - practice
date: 2025-11-17T19:46:49.523412
---
**Exercise 1: Profiling a Slow Python Script**

*Objective:* Profile Python applications to identify performance bottlenecks

---

### Instructions:

1. Download the provided script `slow_script.py` (a script that performs some heavy computation with inefficient loops and data handling).
2. Run the script and note the total runtime.
3. Use Python’s built-in `cProfile` module to profile the execution of the script.
4. Analyze the output to identify which functions or code blocks consume the most time.
5. Use the `pstats` module or `snakeviz` (optional) to visualize the profiling results.
6. Write a short summary (3-4 sentences) describing the main bottlenecks found.

---

### Acceptance Criteria:

- You have successfully run `cProfile` on the script.
- You identified at least two functions or code blocks responsible for the majority of execution time.
- You provide a summary explaining why those parts are slow.

---

### Hints:

- Run profiling with: `python -m cProfile -s time slow_script.py`
- Use `snakeviz` (`pip install snakeviz`) for easier visualization: `python -m cProfile -o output.prof slow_script.py` then `snakeviz output.prof`
- Look for functions with high cumulative time.

---

**Exercise 2: Algorithm Optimization & Efficient Data Structures**

*Objective:* Optimize algorithms and choose efficient data structures

---

### Instructions:

1. The provided function `find_duplicates_naive` uses nested loops to find duplicates in a large list.
2. Rewrite the function to improve its performance using Python data structures (e.g., sets or dictionaries).
3. Test the function on a list of 1 million integers with some duplicates.
4. Measure and compare the runtime of the original and optimized functions using `timeit`.
5. Document your optimization approach and the observed speedup.

---

### Acceptance Criteria:

- Your optimized function returns the correct list of duplicates.
- The optimized function runs significantly faster (at least 5x speedup on large inputs).
- You provide a brief explanation of the data structure choice.

---

### Hints:

- Using a set can reduce lookup time from O(n) to O(1).
- Avoid nested loops when possible.
- Use `timeit.timeit()` with a suitable number of runs.

---

**Exercise 3: Memory Management and Garbage Collection**

*Objective:* Implement memory management and garbage collection strategies

---

### Instructions:

1. Write a Python script that creates a large number of objects referencing each other (e.g., circular references).
2. Use the `gc` module to detect and collect garbage manually.
3. Measure the memory usage of your script before and after invoking garbage collection (using `tracemalloc` or `psutil`).
4. Modify your code to break circular references explicitly and compare the memory impact.
5. Write a short report explaining how circular references affect memory and how Python’s garbage collector deals with them.

---

### Acceptance Criteria:

- You demonstrate creation of circular references.
- You manually trigger garbage collection and observe memory changes.
- You break circular references and show improved memory usage.
- The report correctly explains garbage collection behavior.

---

### Hints:

- Use `gc.collect()` to force garbage collection.
- Enable debugging with `gc.set_debug(gc.DEBUG_LEAK)`.
- Circular references can prevent reference counting from freeing objects immediately.

---

**Exercise 4: Caching and Memoization**

*Objective:* Apply caching and memoization techniques effectively

---

### Instructions:

1. Implement a recursive Fibonacci function without memoization and measure its runtime for `fib(35)`.
2. Apply memoization using `functools.lru_cache` decorator to optimize the Fibonacci function.
3. Measure the runtime again and compare.
4. Next, implement your own simple memoization decorator.
5. Test your decorator on a computationally expensive function (e.g., factorial with delay).
6. Write a brief explanation of caching benefits and potential pitfalls.

---

### Acceptance Criteria:

- The memoized Fibonacci function runs significantly faster than the naive version.
- Your custom memoization decorator caches results correctly.
- The explanation covers cache hits, misses, and cache size considerations.

---

### Hints:

- Use `from functools import lru_cache`.
- To simulate delay, use `time.sleep()` inside the function.
- Be careful with mutable arguments when memoizing.

---

**Exercise 5: Parallel Processing and Async Programming**

*Objective:* Use parallel processing and async programming patterns

---

### Instructions:

1. You are provided a CPU-bound function `compute_prime_factors(n)`.
2. Write a script that computes prime factors for a list of 100 large numbers sequentially and measure the total execution time.
3. Rewrite the script using the `concurrent.futures.ProcessPoolExecutor` to parallelize the factorization.
4. Measure and compare the execution time with the sequential version.
5. Next, simulate an I/O-bound task (e.g., fetching URLs with `asyncio` and `aiohttp`).
6. Write an async function to fetch multiple URLs concurrently and measure the total time.
7. Write a summary comparing parallel processing vs async programming use cases.

---

### Acceptance Criteria:

- Parallel processing reduces CPU-bound task runtime significantly.
- Async programming improves the total time for I/O-bound tasks.
- The summary correctly differentiates CPU-bound vs I/O-bound concurrency.

---

### Hints:

- Use `time.perf_counter()` for timing.
- CPU-bound tasks benefit from multiprocessing, not threading.
- Use `asyncio.run()` to run async functions.
- For async HTTP, install `aiohttp` (`pip install aiohttp`).

---

These exercises will guide you through practical performance profiling and optimization techniques in Python, building up from identifying bottlenecks to applying advanced concurrency patterns.