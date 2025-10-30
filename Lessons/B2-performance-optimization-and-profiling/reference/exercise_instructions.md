# Performance Optimization and Profiling Exercises

## Exercise 1: Profiling a Python Application

### Objective:
Profile a simple Python application to identify performance bottlenecks.

### Instructions:
1. **Download the Sample Application**:
   Clone the following GitHub repository containing a sample Python application that performs matrix multiplication:
   ```bash
   git clone https://github.com/example/matrix-multiplication.git
   cd matrix-multiplication
   ```

2. **Install Required Libraries**:
   If not already installed, set up a virtual environment and install `line_profiler`:
   ```bash
   python -m venv env
   source env/bin/activate
   pip install line_profiler numpy
   ```

3. **Profile the Application**:
   - Open `matrix_multiply.py` and identify the function that performs multiplication.
   - Decorate the multiplication function with the `@profile` decorator from `line_profiler`.
   - Run the profiler using:
     ```bash
     kernprof -l -v matrix_multiply.py
     ```

4. **Analyze the Output**:
   - Review the profiling output to identify which lines of code are the slowest.
   - Note down the function execution times.

### Acceptance Criteria:
- The profiler runs without errors.
- You can identify at least one performance bottleneck in the code.

### Hints:
- Look for functions that take a long time relative to others.
- Ensure `line_profiler` is correctly installed and imported.

---

## Exercise 2: Optimize Algorithms and Data Structures

### Objective:
Optimize a sorting algorithm using more efficient data structures.

### Instructions:
1. **Implement a Sorting Algorithm**:
   - In a new Python file named `sorter.py`, implement a basic bubble sort algorithm.

2. **Profile the Sorting Algorithm**:
   - Use the profiling steps from Exercise 1 to profile your bubble sort implementation.

3. **Optimize the Sorting Algorithm**:
   - Replace the bubble sort with a more efficient sorting algorithm such as quicksort or mergesort.
   - Implement your optimized sorting algorithm in the same file.

4. **Compare Performance**:
   - Profile the optimized algorithm and compare the execution time with the bubble sort.

### Acceptance Criteria:
- You must have both the inefficient and efficient sorting algorithms in your code.
- The optimized sorting algorithm should show a significant performance improvement.

### Hints:
- Revisit sorting algorithm complexities if unsure about their performance.
- Make sure to test your sorting algorithms with large datasets.

---

## Exercise 3: Memory Management and Garbage Collection

### Objective:
Understand and implement memory management strategies.

### Instructions:
1. **Create a Memory-Intensive Application**:
   - Write a Python script that creates a large list of objects (e.g., a list of dictionaries with random data).

2. **Monitor Memory Usage**:
   - Use the `memory_profiler` library to monitor memory usage. Install it with:
     ```bash
     pip install memory-profiler
     ```
   - Decorate the main function with `@profile` and run the script.

3. **Implement Manual Garbage Collection**:
   - Use the `gc` module to manually delete objects that are no longer required.
   - Run the script again and observe any changes in memory usage.

### Acceptance Criteria:
- The memory profile is generated, showing memory consumption over time.
- You can demonstrate a decrease in memory usage after implementing garbage collection.

### Hints:
- Check which objects are consuming the most memory.
- Use the `gc.collect()` function to trigger garbage collection.

---

## Exercise 4: Caching and Memoization Techniques

### Objective:
Apply caching and memoization techniques to optimize a Fibonacci sequence calculation.

### Instructions:
1. **Create a Fibonacci Function**:
   - Write a simple recursive function to calculate Fibonacci numbers in a new file named `fibonacci.py`.

2. **Profile the Recursive Fibonacci**:
   - Profile the initial recursive implementation to measure its performance.

3. **Implement Memoization**:
   - Modify your Fibonacci function to use memoization. You can use a dictionary to store previously computed values.

4. **Profile the Memoized Function**:
   - Profile the new implementation and compare the execution times of both versions.

### Acceptance Criteria:
- You can demonstrate a significant performance improvement in the memoized version.
- The profiler output must clearly show reduced execution time.

### Hints:
- Use decorators like `functools.lru_cache` for easier memoization.
- Ensure input values are large enough to see the difference in performance.

---

## Exercise 5: Parallel Processing and Async Programming

### Objective:
Use parallel processing and asynchronous programming patterns to enhance performance.

### Instructions:
1. **Create a CPU-bound Task**:
   - Write a Python script named `cpu_intensive.py` that performs a CPU-intensive calculation (like calculating prime numbers).

2. **Implement Multiprocessing**:
   - Use Python's `multiprocessing` module to divide the task into multiple processes.
   - Create a function to manage the distribution of tasks across processes.

3. **Implement Async Programming**:
   - Modify your script to implement async programming using `asyncio` to handle I/O-bound tasks (like fetching data from an API).

4. **Measure Performance**:
   - Use `time` module to measure and compare the execution times of both multiprocessing and async implementations.

### Acceptance Criteria:
- Both multiprocessing and async implementations are functional.
- Performance metrics indicate improved execution time for both methods.

### Hints:
- Look into `asyncio.gather()` for managing multiple async calls.
- Be aware of the difference between CPU-bound and I/O-bound tasks when choosing the method of optimization.

---

These exercises will help learners understand and apply performance optimization techniques in Python, providing a hands-on approach to tackling performance challenges.