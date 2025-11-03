## Exercise Set: Regular Expressions and Text Processing

### Exercise 1: Basic Pattern Matching with `re` Module
**Objective:** Familiarize yourself with the `re` module, patterns, and groups.

#### Instructions:
1. Create a Python script named `basic_regex.py`.
2. Import the `re` module.
3. Write a function `find_dates(text)` that takes a string input and returns all dates in the format `YYYY-MM-DD`.
   - Use the pattern `\d{4}-\d{2}-\d{2}` to match dates.
4. Test the function with a sample string containing various dates.
5. Print the found dates to the console.

#### Acceptance Criteria:
- The function should return a list of dates found in the input string.
- The output should be in the format of a list of strings.

#### Hints:
- Use `re.findall()` to find all occurrences of the pattern.
- Remember to handle cases where there might be no matches.

---

### Exercise 2: Named Groups and Validation
**Objective:** Use named groups and work on validation of input formats.

#### Instructions:
1. Extend your `basic_regex.py` script from Exercise 1.
2. Create a new function `validate_email(email)` that checks if the provided string is a valid email address.
   - Use the regex pattern `(?P<username>[a-zA-Z0-9._%+-]+)@(?P<domain>[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})`.
3. The function should return a dictionary containing the `username` and `domain` if valid, or `None` if invalid.
4. Test the function with various email samples.

#### Acceptance Criteria:
- If valid, the function should return a dictionary with keys `username` and `domain`.
- If invalid, it should return `None`.

#### Hints:
- Use `re.match()` to check for a match at the start of the string.
- Use named groups to retrieve the username and domain.

---

### Exercise 3: Pre-compilation and Performance
**Objective:** Learn about pre-compilation of regex patterns for performance.

#### Instructions:
1. Create a new script named `performance_regex.py`.
2. Write a function `compile_and_find(text, pattern)` that:
   - Takes a string `text` and a regex `pattern` as inputs.
   - Pre-compiles the regex using `re.compile()`.
   - Finds all matches in the provided text using the compiled regex.
3. Compare the performance of this function with an inline regex version by measuring the time it takes to run both methods on a large input string.

#### Acceptance Criteria:
- The function should return all matches found.
- You should print both time taken by inline regex and pre-compiled regex for comparison.

#### Hints:
- Use the `time` module to measure execution time.
- Create a large string by repeating a smaller string multiple times.

---

### Exercise 4: Escaping and Safe Extraction
**Objective:** Safely escape strings and extract data.

#### Instructions:
1. Modify your `basic_regex.py` script to include a new function `extract_keywords(text, keyword)` that:
   - Takes a string `text` and a keyword to extract from the text.
   - Safely escape the keyword using `re.escape()` and create a regex pattern to find occurrences of that keyword.
   - Return a list of positions (start index) where the keyword appears in the text.
2. Test the function with different keywords, including those with special regex characters.

#### Acceptance Criteria:
- The function should return a list of starting indices for the keyword in the text.
- The output should handle keywords that include regex special characters without errors.

#### Hints:
- Use `re.finditer()` to find all occurrences and extract their start indices.
- Remember to use raw strings when creating regex patterns.

---

### Exercise 5: Recognizing the Limitations of Regex
**Objective:** Understand when to prefer structured parsers over regex.

#### Instructions:
1. Create a new script named `structured_parser.py`.
2. Write a function `parse_csv(text)` that:
   - Takes a string containing CSV data (comma-separated values).
   - Uses the `csv` module instead of regex to parse the CSV data into a list of dictionaries, where each dictionary represents a row.
3. Compare the complexity of using regex to extract CSV data versus using the `csv` module.

#### Acceptance Criteria:
- The function should return a list of dictionaries, with keys corresponding to the headers of the CSV.
- Provide a brief written reflection (2-3 sentences) on why regex might not be the best tool for parsing CSV.

#### Hints:
- Use `csv.DictReader` for easy CSV parsing.
- Think about edge cases like commas within quoted strings when considering regex.

---

### Conclusion
By completing these exercises, you will gain a solid understanding of various aspects of regex and text processing in Python, as well as when to use structured parsers instead. Each exercise will build upon the knowledge acquired in the previous one, enhancing your skills incrementally. Happy coding!