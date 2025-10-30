# Exercise Series: Performance Optimization and Profiling in Python

## Overview
This set of exercises is designed to help you practice and master various techniques for optimizing Python applications. Each exercise targets a specific learning objective and builds upon the previous one, allowing you to develop a comprehensive understanding of performance optimization.

### Exercise 1: Profiling Python Applications
**Learning Objective:** Profile Python applications to identify performance bottlenecks.

**Instructions:**
1. **Setup:**
   - Download a sample Python application (e.g., a script that calculates Fibonacci numbers recursively).
   - Ensure you have `cProfile` and `pstats` modules available.

2. **Profile the Application:**
   - Run the application through `cProfile` to generate a profiling report.
   - Use the command: 
     ```bash
     python -m cProfile -o profile_output.prof your_script.py
     ```

3. **Analyze the Output:**
   - Load the profiling data using `pstats` and analyze the function call counts and execution times.
   - Identify at least two functions that are potential bottlenecks.

**Acceptance Criteria:**
- You should have a profiling report saved in `profile_output.prof`.
- A summary of at least two bottlenecks with execution times and call counts should be documented.

**Hints:**
- Pay attention to functions with high cumulative time and those that are called frequently.
- Consider visualizing the output using tools such as `SnakeViz` for better insights.

---

### Exercise 2: Algorithm Optimization
**Learning Objective:** Optimize algorithms and choose efficient data structures.

**Instructions:**
1. **Identify an Inefficient Algorithm:**
   - Use the Fibonacci calculation script from Exercise 1. Replace the recursive function with an inefficient iterative approach (e.g., using a list to store all Fibonacci numbers).

2. **Optimize the Algorithm:**
   - Implement a more efficient algorithm using the formula or memoization.
   - Replace the inefficient function with the optimized version.

3. **Profile and Compare:**
   - Profile both the original and optimized implementations.
   - Compare the execution times and document the results.

**Acceptance Criteria:**
- The optimized function should produce the same results as the original.
- Document the performance improvement in execution time.

**Hints:**
- Remember that memoization can significantly reduce the number of calculations by storing previously computed values.
- Use a simple timer (e.g., `time.time()`) to measure execution duration.

---

### Exercise 3: Memory Management and Garbage Collection
**Learning Objective:** Implement memory management and garbage collection strategies.

**Instructions:**
1. **Create a Memory-Intensive Application:**
   - Write a script that creates a large list of random numbers (e.g., 1 million integers).
   - Perform operations that require significant memory usage (e.g., sorting or filtering).

2. **Monitor Memory Usage:**
   - Use the `memory_profiler` library to track memory usage over time.
   - Annotate your script with `@profile` decorator to monitor memory usage of specific functions.

3. **Implement Garbage Collection:**
   - Explicitly call the garbage collector using the `gc` module after memory-intensive operations.
   - Profile the memory usage before and after garbage collection.

**Acceptance Criteria:**
- Document the memory usage before and after garbage collection.
- Show a reduction in memory footprint after implementing garbage collection.

**Hints:**
- Install the `memory_profiler` library using pip if you haven’t already.
- Use `gc.collect()` to invoke garbage collection manually.

---

### Exercise 4: Caching and Memoization
**Learning Objective:** Apply caching and memoization techniques effectively.

**Instructions:**
1. **Use the `functools.lru_cache`:**
   - Modify your optimized Fibonacci function from Exercise 2 to utilize `lru_cache`.
   - Test the performance difference by calculating Fibonacci numbers for both small and large inputs.

2. **Create a Caching Decorator:**
   - If you have time, implement your own caching decorator using a dictionary to store results of function calls.
   - Compare the performance of your decorator with `lru_cache`.

3. **Profile and Validate:**
   - Profile the performance again and document the differences in execution time.

**Acceptance Criteria:**
- The function using `lru_cache` should show performance improvement over the unoptimized version.
- Document the speedup achieved with caching techniques.

**Hints:**
- Pay attention to how caching works with repeated function calls.
- Use different input sizes to see how caching performs under various conditions.

---

### Exercise 5: Parallel Processing and Async Programming
**Learning Objective:** Use parallel processing and async programming patterns.

**Instructions:**
1. **Implement Parallel Processing:**
   - Modify the Fibonacci script to calculate Fibonacci numbers in parallel using the `concurrent.futures` module.
   - Create a pool of workers and distribute the calculation of Fibonacci numbers across them.

2. **Test Async Programming:**
   - Create an asynchronous function that fetches data from a public API (like JSONPlaceholder) and processes it.
   - Use `asyncio` and `aiohttp` to implement non-blocking I/O.

3. **Profile and Validate:**
   - Profile both the parallel and async implementations, comparing their performance to the sequential version.

**Acceptance Criteria:**
- Both implementations should complete and return the correct results.
- Document the performance improvements in execution time for both parallel and async approaches.

**Hints:**
- Ensure you handle exceptions in async functions properly.
- When using `concurrent.futures`, remember to use the `as_completed()` method to handle results as they are completed.

---

### Conclusion
These exercises aim to provide you with practical experience in profiling and optimizing Python applications. By completing these tasks, you should gain a solid foundation in performance optimization techniques.