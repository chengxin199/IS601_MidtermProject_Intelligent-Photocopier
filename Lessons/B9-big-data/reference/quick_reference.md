---
title: Introduction to big data - Quick Reference
layout: layouts/course.njk
courseId: B9-big-data
tags:
  - reference
  - quick-guide
date: 2025-12-04T15:33:44.434790
---
# Quick Reference Guide: Introduction to Big Data

---

## Course Overview
- **Duration:** 3-4 hours  
- **Level:** Intermediate  
- **Topics:**  
  - Introduction to Big Data  
  - Core Concepts  
  - Advanced Techniques  
  - Best Practices  
  - Summary  

---

## 1. Key Concepts

### What is Big Data?  
- Extremely large datasets that traditional data processing tools cannot handle efficiently.  
- Characterized by **3Vs**:  
  - **Volume:** Massive amount of data  
  - **Velocity:** Speed of data generation and processing  
  - **Variety:** Different data types (structured, unstructured, semi-structured)  

### Big Data Ecosystem Components  
- **Storage:** HDFS, NoSQL databases (HBase, Cassandra)  
- **Processing:** MapReduce, Apache Spark  
- **Data Ingestion:** Kafka, Flume  
- **Analytics:** Hive, Pig, MLlib  

### Core Technologies  
- **Hadoop:** Distributed storage and batch processing framework  
- **Spark:** In-memory data processing engine for faster analytics  
- **NoSQL Databases:** Handle unstructured data with flexible schemas  

---

## 2. Common Patterns & Syntax Examples

### MapReduce Pattern  
- **Map:** Processes input key/value pairs to generate intermediate key/value pairs  
- **Reduce:** Merges all intermediate values associated with the same intermediate key  

**Example (Java MapReduce Mapper):**
```java
public class TokenizerMapper extends Mapper<Object, Text, Text, IntWritable> {
    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();

    public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
        StringTokenizer itr = new StringTokenizer(value.toString());
        while (itr.hasMoreTokens()) {
            word.set(itr.nextToken());
            context.write(word, one);
        }
    }
}
```

### Spark Basic Syntax (PySpark)
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Example").getOrCreate()

# Load data
df = spark.read.csv("data.csv", header=True, inferSchema=True)

# Select and show data
df.select("column1", "column2").show()

# Filter rows
filtered_df = df.filter(df["column1"] > 100)

# Aggregation
df.groupBy("category").count().show()
```

### Hive Query Example
```sql
CREATE TABLE IF NOT EXISTS employees (
  id INT,
  name STRING,
  salary FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';

LOAD DATA INPATH '/user/hive/employees.csv' INTO TABLE employees;

SELECT name, salary FROM employees WHERE salary > 50000;
```

---

## 3. Advanced Techniques

- **Data Partitioning:** Improves query performance by dividing data into segments.  
- **Caching in Spark:** Use `.cache()` to keep data in memory for faster access.  
- **Window Functions:** Perform calculations across sets of rows related to the current row.  
- **Streaming Data Processing:** Real-time data handling using Spark Streaming or Kafka Streams.  

---

## 4. Best Practices

- Use **schema-on-read** for flexibility in data ingestion.  
- Optimize file formats: Use **Parquet** or **ORC** for efficient storage and querying.  
- Monitor cluster resource usage to prevent bottlenecks.  
- Clean and preprocess data before analysis to improve accuracy.  
- Secure data with proper authentication and encryption.  

---

## 5. Troubleshooting Quick Fixes

| Issue                                | Possible Cause                        | Quick Fix                                   |
|------------------------------------|------------------------------------|---------------------------------------------|
| Job fails with OutOfMemoryError     | Insufficient memory allocation      | Increase executor memory or optimize code  |
| Slow query performance              | No partitioning or inefficient joins| Add partitions, use broadcast joins        |
| Data skew in Spark jobs             | Uneven data distribution            | Use salting or repartition data             |
| Connection refused to HDFS          | HDFS service down or network issue  | Check HDFS status, restart services         |
| Kafka consumer not receiving data   | Incorrect topic or offset issues    | Verify topic name, reset offsets if needed  |

---

## Summary

- Big Data deals with large, fast, and diverse datasets requiring specialized tools.  
- Hadoop and Spark are core technologies for storage and processing.  
- Use MapReduce for batch jobs, Spark for in-memory analytics, and Hive for SQL querying.  
- Apply best practices in data format, partitioning, and resource optimization.  
- Quickly troubleshoot common issues by checking memory, partitions, and service statuses.

---

Keep this guide handy during your coding and analysis tasks for quick reminders and syntax help!