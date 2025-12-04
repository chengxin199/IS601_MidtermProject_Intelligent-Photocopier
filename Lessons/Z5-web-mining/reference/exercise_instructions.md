---
title: Advance web mining - Exercise Instructions
layout: layouts/course.njk
courseId: Z5-web-mining
tags:
  - exercises
  - practice
date: 2025-12-03T20:26:46.280996
---
## Exercise 1: Basic Web Scraper for Article Titles
**Difficulty:** Beginner  
**Time Estimate:** 30 minutes

### Objective
Implement a simple web scraper that fetches the HTML content of a webpage and extracts all article titles (e.g., `<h2>` tags with class "title"). This will help you master basic web mining concepts like HTTP requests and HTML parsing.

### Starter Code
```python
import requests
from bs4 import BeautifulSoup

def extract_article_titles(url):
    """
    Fetch the webpage at `url` and extract all article titles inside <h2 class="title"> tags.
    Return a list of strings representing the titles.
    """
    # TODO: Send HTTP GET request to fetch page content
    # TODO: Parse HTML using BeautifulSoup
    # TODO: Find all <h2> tags with class 'title' and extract text
    # TODO: Return list of titles
    pass
```

### Requirements
- Use `requests` to get the page content.
- Parse HTML using `BeautifulSoup`.
- Extract text from all `<h2>` tags with class `"title"`.
- Return an empty list if no titles are found.
- Handle network errors gracefully.

### Test Cases
```python
# Example with a mocked HTML content (simulate requests for testing)
def test_extract_article_titles():
    url = "https://example.com/articles"
    titles = extract_article_titles(url)
    # Expected output depends on actual page content; here is a hypothetical example:
    assert isinstance(titles, list)
    for title in titles:
        assert isinstance(title, str)
    # Edge case: invalid URL or no titles found
    assert extract_article_titles("http://invalid.url") == []
    assert extract_article_titles("https://example.com/no_titles") == []
```

### Hints
- Use `requests.get(url, timeout=5)` to avoid hanging.
- Use `BeautifulSoup(html, "html.parser")` for parsing.
- Use `soup.find_all("h2", class_="title")` to locate title tags.
- Catch exceptions like `requests.exceptions.RequestException` to handle network errors.


---

## Exercise 2: Extract and Clean Text from Multiple Webpages
**Difficulty:** Intermediate  
**Time Estimate:** 45 minutes

### Objective
Extend your scraper to accept a list of URLs, extract article titles and their corresponding summaries (e.g., `<p class="summary">`), and clean the text by removing excessive whitespace and HTML entities.

### Starter Code
```python
import requests
from bs4 import BeautifulSoup
import html

def extract_articles_info(urls):
    """
    Given a list of URLs, extract article titles and summaries from each page.
    Return a list of dictionaries, each with 'title' and 'summary' keys.
    """
    articles = []
    for url in urls:
        # TODO: Fetch page content safely
        # TODO: Parse HTML and extract title and summary
        # TODO: Clean text by removing HTML entities and trimming whitespace
        # TODO: Append dict {'title': title, 'summary': summary} to articles list
        pass
    return articles
```

### Requirements
- Accept a list of URLs as input.
- For each URL, extract `<h2 class="title">` and `<p class="summary">`.
- Clean extracted strings (decode HTML entities, strip whitespace).
- If a summary is missing, use an empty string.
- Return a list of dictionaries with keys `"title"` and `"summary"`.
- Handle network errors and skip URLs that fail to load.

### Test Cases
```python
test_urls = [
    "https://example.com/article1",
    "https://example.com/article2",
    "https://invalid.url"
]

result = extract_articles_info(test_urls)
assert isinstance(result, list)
for article in result:
    assert "title" in article and "summary" in article
    assert isinstance(article["title"], str)
    assert isinstance(article["summary"], str)
```

### Hints
- Use `html.unescape()` to decode HTML entities.
- Use `.strip()` to clean whitespace from strings.
- Use try-except blocks to continue if a URL fetch fails.
- Use `continue` to skip to the next URL on errors.


---

## Exercise 3: Build a Domain-Specific Keyword Frequency Analyzer
**Difficulty:** Advanced  
**Time Estimate:** 60 minutes

### Objective
Build a module that mines multiple webpages in a domain, extracts main textual content, cleans it, and computes keyword frequencies. This will help you apply text mining and natural language processing techniques in web mining.

### Starter Code
```python
import requests
from bs4 import BeautifulSoup
import re
from collections import Counter

def fetch_and_clean_text(url):
    """
    Fetch the webpage content, extract main text (e.g., inside <article> or <div id="content">),
    clean it by removing HTML tags, punctuation, and lowercasing.
    Return cleaned text as a string.
    """
    # TODO: Fetch page content
    # TODO: Extract main content (prefer <article> tag, or fallback to <div id="content">)
    # TODO: Remove HTML tags and punctuation, convert to lowercase
    # TODO: Return cleaned text string
    pass

def compute_keyword_frequency(urls, keywords):
    """
    Given a list of URLs and a list of keywords, compute how often each keyword appears
    across all fetched pages' cleaned text.
    Return a dictionary {keyword: frequency}.
    """
    # TODO: For each URL, fetch and clean text
    # TODO: Count occurrences of each keyword (case-insensitive)
    # TODO: Aggregate counts across all URLs
    pass
```

### Requirements
- Extract main text preferably from `<article>`, fallback to `<div id="content">`.
- Remove all HTML tags and punctuation using regex.
- Normalize text to lowercase.
- Count keyword frequencies considering whole words only.
- Aggregate counts across all URLs.
- Handle URLs that fail gracefully by skipping them.

### Test Cases
```python
urls = [
    "https://example.com/page1",
    "https://example.com/page2"
]
keywords = ["python", "data", "mining"]

freqs = compute_keyword_frequency(urls, keywords)
assert isinstance(freqs, dict)
for kw in keywords:
    assert kw in freqs
    assert isinstance(freqs[kw], int)
    assert freqs[kw] >= 0
```

### Hints
- Use `soup.find("article")` and `soup.find("div", id="content")`.
- Use `re.sub(r'<.*?>', '', html_content)` to remove HTML tags.
- Use `re.findall(r'\bword\b', text)` for whole word matching.
- Use `collections.Counter` to accumulate frequencies.
- Normalize keywords to lowercase before matching.


---

## Exercise 4: Crawl a Website and Build a Link Graph
**Difficulty:** Advanced  
**Time Estimate:** 90 minutes

### Objective
Implement a web crawler that starts from a given URL, follows internal links up to a specified depth, and builds a graph representing page connections (edges are links). This is a core task in advanced web mining for link analysis.

### Starter Code
```python
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import defaultdict

def crawl_website(start_url, max_depth=2):
    """
    Crawl the website starting from start_url up to max_depth.
    Return a dictionary representing the link graph:
    {page_url: set(of linked page URLs)}
    """
    visited = set()
    graph = defaultdict(set)

    def is_internal(url):
        # TODO: Check if url belongs to the same domain as start_url
        pass

    def crawl(url, depth):
        if depth > max_depth or url in visited:
            return
        try:
            # TODO: Fetch page content
            # TODO: Parse and extract all internal links
            # TODO: Add links to graph[url]
            # TODO: Recursively crawl each linked URL
            pass
        except Exception:
            # Skip URLs that cause errors
            pass

    crawl(start_url, 0)
    return graph
```

### Requirements
- Only crawl URLs within the same domain as `start_url`.
- Extract links from `<a href="...">` tags.
- Normalize URLs to absolute URLs using `urljoin`.
- Avoid revisiting URLs.
- Limit crawling by `max_depth`.
- Return graph as a dict of sets mapping URL to linked URLs.

### Test Cases
```python
graph = crawl_website("https://example.com", max_depth=1)
assert isinstance(graph, dict)
for url, links in graph.items():
    assert isinstance(url, str)
    assert isinstance(links, set)
    for link in links:
        assert link.startswith("https://example.com")
```

### Hints
- Use `urlparse` to compare domains.
- Use `urljoin(base, link)` to handle relative URLs.
- Use a recursive helper function with depth control.
- Use sets to avoid duplicate links.
- Handle exceptions to continue crawling other pages.


---

## Exercise 5: Extract Structured Data from HTML Tables and Export to CSV
**Difficulty:** Advanced  
**Time Estimate:** 60 minutes

### Objective
Implement a function that mines all HTML tables from a webpage, extracts their data, and exports each table into a CSV file. This exercise combines web mining with data extraction and storage.

### Starter Code
```python
import requests
from bs4 import BeautifulSoup
import csv

def extract_tables_to_csv(url, output_prefix="table"):
    """
    Fetch the webpage at url, extract all HTML tables, and save each as a CSV file.
    CSV files should be named {output_prefix}_1.csv, {output_prefix}_2.csv, etc.
    """
    # TODO: Fetch page content
    # TODO: Parse HTML and find all <table> tags
    # TODO: For each table, extract headers (if any) and rows
    # TODO: Write each table to a separate CSV file
    pass
```

### Requirements
- Extract all `<table>` elements.
- Handle tables with and without `<thead>`.
- Extract data from `<th>` and `<td>` cells.
- Handle rowspan and colspan by repeating cells accordingly (optional for bonus).
- Save each table in a separate CSV file.
- Handle pages with no tables gracefully (no files created).

### Test Cases
```python
extract_tables_to_csv("https://example.com/data_page", output_prefix="data")

# Check that files data_1.csv, data_2.csv, ... exist if tables present
# If no tables, no files should be created
```

### Hints
- Use `soup.find_all("table")` to get tables.
- Use `.find_all("tr")` to iterate rows.
- Use `.find_all(["th", "td"])` to get cells.
- For CSV writing, use Python's `csv.writer`.
- Consider edge cases like empty tables or irregular rows.

---

These exercises cover foundational and advanced tasks in web mining: from data extraction, cleaning, crawling, analysis, to exporting structured data. Each builds on the previous to develop full practical skills.