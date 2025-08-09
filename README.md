# Task 1: Extension of Trie Functionality

This project extends the functionality of a prefix tree (Trie) by implementing two additional methods:

- **count_words_with_suffix(pattern)** — counts how many words stored in the Trie end with the given suffix `pattern`.
- **has_prefix(prefix)** — checks whether there exists at least one word in the Trie that starts with the given prefix `prefix`.


## Technical Requirements

- Class `Homework` inherits from `Trie`.
- Input parameters are strings; invalid types raise exceptions.
- Methods must be case-sensitive.
- Efficient for large datasets.


## Running the Program

```bash
cd functionality_expansion
python functionality_expansion.py
```
---

# Task 2. Longest Common Prefix Search

## Description

Create a class `LongestCommonWord` that inherits from the `Trie` class and implements the method `find_longest_common_word`, which finds the longest common prefix among all the words in the input array of strings `strings`.

## Technical Requirements

- The class `LongestCommonWord` must inherit from `Trie`.
- The input parameter of the method `find_longest_common_word`, `strings`, is an array of strings.
- The method `find_longest_common_word` should return a string — the longest common prefix.
- Time complexity — **O(S)**, where **S** is the total length of all strings.


## Running the Program

```bash
cd longest_common
python longest_common.py
```
