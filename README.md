# Task 1: Extension of Trie Functionality

This project extends the functionality of a prefix tree (Trie) by implementing two additional methods:

- **count_words_with_suffix(pattern)** — counts how many words stored in the Trie end with the given suffix `pattern`.
- **has_prefix(prefix)** — checks whether there exists at least one word in the Trie that starts with the given prefix `prefix`.


## Requirements

- Class `Homework` inherits from `Trie`.
- Input parameters are strings; invalid types raise exceptions.
- Methods must be case-sensitive.
- Efficient for large datasets.


## Acceptance Criteria

1. `count_words_with_suffix(pattern)` returns the number of words that end with the exact suffix `pattern`. If no such words exist, it returns 0. It is case-sensitive.  
2. `has_prefix(prefix)` returns `True` if there is at least one word starting with the exact prefix `prefix`. Otherwise, it returns `False`. It is case-sensitive.  
3. The code passes all tests.  
4. Incorrect input types are properly handled with exceptions.  
5. The methods work efficiently with large datasets.

## Running the Program

```bash
cd functionality_expansion
python functionality_expansion.py
```
---

