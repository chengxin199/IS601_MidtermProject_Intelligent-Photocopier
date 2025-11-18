---
title: Performance Optimization and Profiling - Quick Reference
layout: layouts/base.njk
courseId: B2-performance-optimization-and-profiling
tags:
  - reference
  - quick-guide
date: 2025-11-17T19:46:22.698558
---
# Performance Optimization and Profiling — Quick Reference Guide

---

## Course Overview  
**Duration:** 4-5 hours  
**Level:** Intermediate  
**Focus:** Techniques and tools to analyze, optimize, and improve code performance through profiling and best practices.

---

## 1. Key Concepts

- **Performance Optimization:** Improving code efficiency to reduce execution time, memory usage, and resource consumption.  
- **Profiling:** Measuring program behavior (CPU, memory, I/O) to identify bottlenecks.  
- **Hotspots:** Code sections where most time is spent, prime candidates for optimization.  
- **Latency vs Throughput:** Latency = time per operation; Throughput = operations per unit time.  
- **Big O Notation:** Describes algorithmic complexity and scalability.  
- **Caching:** Storing computed results to avoid redundant work.  
- **Lazy Evaluation:** Deferring computation until necessary to save resources.  
- **Inlining:** Replacing a function call with the function code to reduce call overhead.  
- **Memory Leaks:** Unreleased memory causing increased usage and slowdowns.  

---

## 2. Common Patterns & Syntax Examples

### a. Measuring Execution Time (Python example)

```python
import time

start = time.perf_counter()
# Code block to measure
end = time.perf_counter()
print(f"Elapsed time: {end - start:.6f} seconds")
```

### b. Using a Profiler (Python `cProfile`)

```bash
python -m cProfile -s time your_script.py
```

### c. Memoization (Caching) Pattern

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### d. Avoiding Unnecessary Loops

**Inefficient:**

```python
result = []
for item in data:
    if expensive_check(item):
        result.append(item)
```

**Optimized using list comprehension:**

```python
result = [item for item in data if expensive_check(item)]
```

---

## 3. Code Snippets for Optimization

### Loop Optimization

```python
# Inefficient: repeated attribute lookup
for i in range(len(my_list)):
    print(my_list[i])

# Optimized: cache length
length = len(my_list)
for i in range(length):
    print(my_list[i])
```

### String Concatenation

```python
# Inefficient
s = ""
for word in words:
    s += word + " "

# Optimized
s = " ".join(words)
```

### Using Generators to Save Memory

```python
# List comprehension (memory-heavy)
squares = [x*x for x in range(1000000)]

# Generator expression (memory-efficient)
squares = (x*x for x in range(1000000))
```

---

## 4. Troubleshooting Quick Fixes

| Issue                          | Cause                              | Quick Fix                                  |
|-------------------------------|----------------------------------|--------------------------------------------|
| Slow startup time              | Heavy imports or initialization  | Lazy load modules, defer initialization    |
| High CPU usage                 | Inefficient algorithms/loops     | Profile code, optimize hotspots            |
| Memory bloat/leak              | Unreleased references             | Use memory profilers, fix references       |
| Blocking I/O                   | Synchronous calls                 | Use async I/O or multithreading             |
| Excessive logging overhead     | Verbose logging in hot paths     | Reduce logging level or disable in prod    |
| Repeated expensive calculations| No caching                      | Implement memoization or caching            |
| Large data structure iteration | Inefficient data structures      | Use appropriate data structures (sets, dicts) |

---

## 5. Profiling Tools & Commands

| Tool/Library       | Purpose                      | Usage Example                        |
|--------------------|------------------------------|------------------------------------|
| `cProfile` (Python) | CPU profiling                | `python -m cProfile script.py`     |
| `memory_profiler`   | Memory usage tracking        | Add `@profile` decorator + run with `mprof run script.py` |
| `line_profiler`    | Line-by-line profiling        | Decorate functions with `@profile` |
| Chrome DevTools    | JS performance profiling      | Open DevTools → Performance tab    |
| VisualVM (Java)    | CPU and memory profiling      | Attach to JVM process               |

---

## 6. Best Practices Summary

- Profile **before** optimizing — identify real bottlenecks.  
- Focus on **hotspots**, not premature optimization.  
- Use efficient algorithms and data structures.  
- Minimize I/O and network calls in critical paths.  
- Cache results of expensive operations.  
- Avoid global variables and large memory footprints.  
- Use built-in language features optimized in C (e.g., Python’s `join`).  
- Test performance impact after changes.

---

Keep this guide handy during coding sessions to quickly identify and fix performance issues!