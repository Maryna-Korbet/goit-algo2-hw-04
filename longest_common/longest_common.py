class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to hold child nodes
        self.is_end = False  # Indicates the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def put(self, word, value=None):
        """
        Inserts a word into the Trie.

        Args:
            word (str): The word to insert.
            value (optional): Not used currently, but can store additional info.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True  # Mark the end of the word

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        """
        Finds the longest common prefix among a list of strings using Trie.

        Args:
            strings (list[str]): List of strings to find the common prefix for.

        Returns:
            str: The longest common prefix. Empty string if none found or input invalid.
        """
        if not strings or not all(isinstance(word, str) for word in strings):
            print("Invalid input: Expected a list of strings.")
            return ""
        
        if len(strings) == 1:
            print(f"Only one word provided: {strings[0]}")
            return strings[0]
        
        # Insert all words into the Trie
        for word in strings:
            self.put(word, True)
        
        node = self.root
        prefix = ""
        
        # Traverse the Trie while there's exactly one child and it's not the end of a word
        while node and len(node.children) == 1 and not node.is_end:
            char = next(iter(node.children))  # Get the single child character
            prefix += char
            node = node.children[char]

        print(f"Longest common prefix found: '{prefix}'")
        return prefix


if __name__ == "__main__":
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    print("Test 1: ", strings)
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    print("Test 2: ", strings)
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    print("Test 3: ", strings)
    assert trie.find_longest_common_word(strings) == ""

    print("All tests passed!")
