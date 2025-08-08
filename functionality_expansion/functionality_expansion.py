from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        """
        Counts how many words in the Trie end with the specified suffix pattern.
        
        Args:
            pattern (str): The suffix string to match.
        
        Returns:
            int: Number of words ending with the given suffix.
        
        Raises:
            ValueError: If the input pattern is not a string.
        """
        if not isinstance(pattern, str):
            raise ValueError("Pattern must be a string")
        
        count = 0
        for word in self.get_all_words():  
            if word.endswith(pattern):
                count += 1
                print(f"Words ending with '{pattern}': {count}")
        return count

    def has_prefix(self, prefix) -> bool:
        """
        Checks whether there is at least one word in the Trie starting with the specified prefix.
        
        Args:
            prefix (str): The prefix string to check.
        
        Returns:
            bool: True if any word starts with the prefix, False otherwise.
        
        Raises:
            ValueError: If the input prefix is not a string.
        """
        if not isinstance(prefix, str):
            raise ValueError("Prefix must be a string")
        
        result = bool(self.keys_with_prefix(prefix))  
        print(f"Prefix '{prefix}' exists in the Trie: {result}")
        return result
    

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    print("All words in Trie:", trie.get_all_words())

    # Checking the number of words ending with a given suffix
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Checking for the presence of a prefix
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat