---
title: Advance web mining - Practice Solution
layout: layouts/base.njk
courseId: Z5-web-mining
tags:
  - solutions
  - code
date: 2025-12-03T20:27:59.308738
---
# Advanced Web Mining Practice Solutions

This document covers advanced exercises in web mining, designed to help you:

- Master key concepts such as web scraping, crawling, and data extraction
- Apply practical techniques using Python libraries
- Build real-world projects that are robust and maintainable

---

## Exercise 1: Build a Robust Web Crawler to Extract Article Titles and URLs from a News Website

### Overview

In this exercise, we will implement a web crawler that fetches article titles and URLs from a news site’s homepage. We will start with a basic crawler using `requests` and `BeautifulSoup`, then enhance it with error handling, rate limiting, and user-agent headers to avoid getting blocked.

---

### Basic Implementation

```python
import requests
from bs4 import BeautifulSoup

def fetch_articles_basic(url):
    """
    Fetch article titles and URLs from the given news homepage.
    
    Args:
        url (str): URL of the news homepage.
    
    Returns:
        list of dict: List of articles with keys 'title' and 'url'.
    """
    # Send GET request to the URL
    response = requests.get(url)
    
    # Parse HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all article links (assuming they are inside <a> tags with a class 'article-link')
    articles = []
    for link in soup.find_all('a', class_='article-link'):
        title = link.get_text(strip=True)
        href = link.get('href')
        articles.append({'title': title, 'url': href})
    return articles
```

---

### Enhanced Implementation

```python
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin

def fetch_articles_enhanced(url, max_retries=3, timeout=5):
    """
    Enhanced crawler to fetch article titles and URLs with error handling and politeness.
    
    Args:
        url (str): URL of the news homepage.
        max_retries (int): Number of retries on failure.
        timeout (int): Request timeout in seconds.
    
    Returns:
        list of dict: List of articles with keys 'title' and 'url'.
    
    Raises:
        ValueError: If the URL is invalid.
        requests.RequestException: For network-related errors.
    """
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' 
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/112.0.0.0 Safari/537.36'
        )
    }
    if not url.startswith(('http://', 'https://')):
        raise ValueError('Invalid URL. Must start with http:// or https://')

    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()  # Raise HTTPError for bad status codes
            break  # Success
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt == max_retries - 1:
                raise
            time.sleep(2)  # wait before retrying

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []
    for link in soup.find_all('a', class_='article-link'):
        title = link.get_text(strip=True)
        href = link.get('href')
        # Convert relative URLs to absolute URLs
        full_url = urljoin(url, href)
        articles.append({'title': title, 'url': full_url})
    
    # Be polite and wait between requests (if crawling multiple pages)
    time.sleep(1)
    return articles
```

---

### Testing the Solution

```python
def test_fetch_articles_basic():
    # Sample HTML snippet to simulate fetched content
    html = """
    <html>
      <body>
        <a class="article-link" href="/news/1">Article One</a>
        <a class="article-link" href="/news/2">Article Two</a>
      </body>
    </html>
    """
    from bs4 import BeautifulSoup

    def mock_requests_get(url):
        class MockResponse:
            def __init__(self, text):
                self.text = text
        return MockResponse(html)
    
    # Patch requests.get temporarily
    import types
    original_get = requests.get
    requests.get = mock_requests_get
    
    articles = fetch_articles_basic('http://fakeurl.com')
    assert articles == [
        {'title': 'Article One', 'url': '/news/1'},
        {'title': 'Article Two', 'url': '/news/2'}
    ], "Basic fetch_articles_basic test failed"
    
    # Restore requests.get
    requests.get = original_get
    print("Basic test passed.")

def test_fetch_articles_enhanced():
    # For enhanced, test URL validation and error handling
    try:
        fetch_articles_enhanced('ftp://invalid-url.com')
    except ValueError as e:
        assert str(e) == 'Invalid URL. Must start with http:// or https://'
    else:
        assert False, "URL validation failed"

    # Test network error handling by simulating failed requests
    import requests

    def mock_fail_get(*args, **kwargs):
        raise requests.ConnectionError("Network unreachable")

    original_get = requests.get
    requests.get = mock_fail_get

    try:
        fetch_articles_enhanced("http://example.com", max_retries=2)
    except requests.RequestException:
        print("Network error handling test passed.")
    else:
        assert False, "Error handling for network failure failed"

    requests.get = original_get

test_fetch_articles_basic()
test_fetch_articles_enhanced()
```

---

### Explanation

- **Design Decisions:**
  - Used `requests` for HTTP requests and `BeautifulSoup` for parsing HTML.
  - Added retries and timeout to handle unreliable networks.
  - Added user-agent headers to mimic real browsers and reduce blocking.
  - Used `urljoin` to handle relative URLs properly.
  - Included polite waiting to avoid hammering servers.

- **Key Concepts:**
  - Web scraping basics: HTTP requests, parsing DOM elements.
  - Robustness: retries, error handling.
  - URL normalization.

- **Complexity:**
  - Time complexity depends on the number of articles on the page (O(n)).
  - Network latency dominates actual runtime.

---

### Key Takeaways

- Always validate URLs before making requests.
- Use headers to avoid blocks by websites.
- Properly handle relative URLs with `urljoin`.
- Implement error handling and retries for network resilience.
- Be polite: respect site crawling policies and add delays.
- Modular code helps in testing and future enhancements.

---

## Exercise 2: Implement a Focused Crawler That Extracts Links Only Within a Specific Domain

### Overview

Focused crawling narrows down the crawl scope to a specific domain or topic. We will build a crawler that recursively visits pages within a domain and extracts all URLs limited to that domain.

---

### Basic Implementation

```python
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def focused_crawl_basic(start_url, max_pages=10):
    """
    Basic focused crawler that collects URLs within the same domain.
    
    Args:
        start_url (str): Starting URL for crawling.
        max_pages (int): Max number of pages to crawl.
    
    Returns:
        set: Unique URLs found within the domain.
    """
    domain = urlparse(start_url).netloc
    to_crawl = [start_url]
    crawled = set()
    
    while to_crawl and len(crawled) < max_pages:
        url = to_crawl.pop()
        crawled.add(url)
        
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a', href=True):
                href = urljoin(url, link['href'])
                href_domain = urlparse(href).netloc
                if href_domain == domain and href not in crawled and href not in to_crawl:
                    to_crawl.append(href)
        except Exception:
            # Ignore errors in basic version
            continue
    
    return crawled
```

---

### Enhanced Implementation

```python
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import time

def focused_crawl_enhanced(start_url, max_pages=10, timeout=5, max_retries=3):
    """
    Enhanced focused crawler with error handling, retries, and politeness.
    
    Args:
        start_url (str): URL to start crawling.
        max_pages (int): Maximum pages to crawl.
        timeout (int): Request timeout.
        max_retries (int): Number of retries on failure.
    
    Returns:
        set: Unique URLs crawled within domain.
    """
    domain = urlparse(start_url).netloc
    to_crawl = [start_url]
    crawled = set()
    headers = {
        'User-Agent': 'AdvancedWebMinerBot/1.0 (+https://example.com/bot)'
    }
    
    while to_crawl and len(crawled) < max_pages:
        url = to_crawl.pop()
        if url in crawled:
            continue
        
        for attempt in range(max_retries):
            try:
                response = requests.get(url, headers=headers, timeout=timeout)
                response.raise_for_status()
                break
            except requests.RequestException as e:
                print(f"Error fetching {url}: {e}")
                if attempt == max_retries - 1:
                    response = None
                else:
                    time.sleep(1)
        if response is None:
            continue
        
        crawled.add(url)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = urljoin(url, link['href'])
            href_domain = urlparse(href).netloc
            if href_domain == domain and href not in crawled and href not in to_crawl:
                to_crawl.append(href)
        
        time.sleep(0.5)  # Politeness delay
    
    return crawled
```

---

### Testing the Solution

```python
def test_focused_crawl_basic():
    # Setup a mock HTTP server or simulate requests.get with predefined HTML pages
    html_page_1 = """
    <html><body>
    <a href="http://example.com/page2">Page 2</a>
    <a href="http://external.com/page">External</a>
    </body></html>
    """
    html_page_2 = """
    <html><body>
    <a href="http://example.com/page3">Page 3</a>
    </body></html>
    """
    
    class MockResponse:
        def __init__(self, text):
            self.text = text
    
    def mock_requests_get(url):
        if url == "http://example.com":
            return MockResponse(html_page_1)
        elif url == "http://example.com/page2":
            return MockResponse(html_page_2)
        else:
            raise requests.ConnectionError("URL not found")
    
    original_get = requests.get
    requests.get = mock_requests_get
    
    crawled_urls = focused_crawl_basic("http://example.com", max_pages=5)
    expected = {
        "http://example.com",
        "http://example.com/page2",
        "http://example.com/page3"
    }
    assert crawled_urls == expected, "Basic focused crawl test failed"
    
    requests.get = original_get
    print("Basic focused crawl test passed.")

def test_focused_crawl_enhanced():
    # Test invalid URL
    try:
        focused_crawl_enhanced("ftp://example.com")
    except Exception as e:
        print(f"Caught expected exception for invalid URL: {e}")

    # Test network error retries
    def mock_fail_get(*args, **kwargs):
        raise requests.ConnectionError("Network down")
    
    original_get = requests.get
    requests.get = mock_fail_get

    urls = focused_crawl_enhanced("http://example.com", max_pages=2)
    assert urls == set(), "Enhanced crawl should return empty set on failure"
    
    requests.get = original_get
    print("Enhanced focused crawl tests passed.")

test_focused_crawl_basic()
test_focused_crawl_enhanced()
```

---

### Explanation

- **Design Decisions:**
  - Depth-first crawling using a stack (`to_crawl` list).
  - Restrict crawling to URLs with same domain to keep scope focused.
  - Added politeness delays and error retries in enhanced version.
  - Use of HTTP headers to identify crawler.

- **Key Concepts:**
  - URL normalization and domain extraction.
  - Crawling strategies: keeping track of visited and to-visit URLs.
  - Handling broken links and network errors gracefully.

- **Complexity:**
  - Time complexity depends on max_pages and network latency.
  - Space complexity proportional to number of URLs tracked.

---

### Key Takeaways

- Always keep track of visited URLs to avoid loops.
- Limit crawl scope to avoid crawling the entire web.
- Implement retries and error handling to deal with unstable networks.
- Use delays to respect server resources.
- Configure user-agent strings to identify your crawler.

---

## Exercise 3: Extract Structured Data from Web Pages using XPath and JSON-LD

### Overview

Many modern websites embed structured data using JSON-LD scripts or have well-defined HTML structures accessible via XPath. This exercise demonstrates how to extract structured data using both methods.

---

### Basic Implementation (Using XPath with lxml)

```python
import requests
from lxml import html

def extract_titles_with_xpath(url):
    """
    Extract article titles using XPath queries.
    
    Args:
        url (str): URL of the web page.
    
    Returns:
        list: List of article titles extracted.
    """
    response = requests.get(url)
    tree = html.fromstring(response.content)
    
    # Example XPath for article titles - this must be adapted per site
    titles = tree.xpath('//h2[@class="article-title"]/text()')
    return [t.strip() for t in titles if t.strip()]
```

---

### Enhanced Implementation (JSON-LD Extraction + Error Handling)

```python
import requests
from lxml import html
import json

def extract_structured_data(url, timeout=5):
    """
    Extract structured data from page JSON-LD and XPath, with error handling.
    
    Args:
        url (str): URL of the web page.
        timeout (int): Request timeout in seconds.
    
    Returns:
        dict: {
            'titles_xpath': list of titles from XPath,
            'jsonld': list of JSON-LD objects found
        }
    """
    headers = {'User-Agent': 'AdvancedWebMinerBot/1.0'}
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return {'titles_xpath': [], 'jsonld': []}
    
    try:
        tree = html.fromstring(response.content)
    except Exception as e:
        print(f"Failed to parse HTML: {e}")
        return {'titles_xpath': [], 'jsonld': []}
    
    titles = tree.xpath('//h2[@class="article-title"]/text()')
    titles = [t.strip() for t in titles if t.strip()]
    
    jsonld_data = []
    scripts = tree.xpath('//script[@type="application/ld+json"]/text()')
    for script in scripts:
        try:
            data = json.loads(script)
            if isinstance(data, list):
                jsonld_data.extend(data)
            else:
                jsonld_data.append(data)
        except json.JSONDecodeError:
            continue
    
    return {'titles_xpath': titles, 'jsonld': jsonld_data}
```

---

### Testing the Solution

```python
def test_extract_titles_with_xpath():
    html_content = """
    <html><body>
        <h2 class="article-title">Title One</h2>
        <h2 class="article-title">Title Two</h2>
    </body></html>
    """
    from lxml import html as lxml_html

    def mock_requests_get(url):
        class MockResponse:
            def __init__(self, content):
                self.content = content.encode('utf-8')
        return MockResponse(html_content)
    
    original_get = requests.get
    requests.get = mock_requests_get
    
    titles = extract_titles_with_xpath("http://fakeurl.com")
    assert titles == ["Title One", "Title Two"], "XPath basic extraction failed"
    
    requests.get = original_get
    print("XPath basic extraction test passed.")

def test_extract_structured_data():
    html_content = """
    <html><head>
    <script type="application/ld+json">
    {
        "@context": "http://schema.org",
        "@type": "NewsArticle",
        "headline": "Sample Article"
    }
    </script>
    </head><body>
        <h2 class="article-title">Title From XPath</h2>
    </body></html>
    """
    
    def mock_requests_get(url, headers=None, timeout=None):
        class MockResponse:
            def __init__(self, content):
                self.content = content.encode('utf-8')
            def raise_for_status(self):
                pass
        return MockResponse(html_content)
    
    original_get = requests.get
    requests.get = mock_requests_get
    
    data = extract_structured_data("http://fakeurl.com")
    assert data['titles_xpath'] == ["Title From XPath"]
    assert any(d.get("@type") == "NewsArticle" for d in data['jsonld'])
    
    requests.get = original_get
    print("Structured data extraction test passed.")

test_extract_titles_with_xpath()
test_extract_structured_data()
```

---

### Explanation

- **Design Decisions:**
  - Used `lxml` for XPath support (more powerful than BeautifulSoup for XPath).
  - Extracted JSON-LD embedded data by parsing `<script type="application/ld+json">`.
  - Added error handling for network and parsing errors.

- **Key Concepts:**
  - XPath queries for HTML element extraction.
  - Structured data in JSON-LD format.
  - Parsing and handling JSON embedded in HTML.

- **Complexity:**
  - XPath extraction is linear with respect to document size.
  - JSON parsing complexity depends on JSON size.

---

### Key Takeaways

- Use XPath for precise extraction when element structure is known.
- JSON-LD provides rich metadata; parse it to get structured info.
- Always handle exceptions in network and parsing steps.
- Use robust libraries (`lxml`) to leverage XPath support.

---

# Summary

This document provided comprehensive advanced web mining exercises, including crawling, focused crawling, and structured data extraction with:

- Progressive implementations (basic → enhanced)
- Detailed inline comments
- Proper error handling and validation
- Unit-testing examples
- Alternative approaches and design explanations

Mastering these techniques equips you to build scalable and maintainable web mining solutions in production.