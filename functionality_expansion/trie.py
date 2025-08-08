class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        """
        Initialize the root node of the Trie.
        """
        self.root = TrieNode()

    def put(self, key, val=None):
        """
        Insert a word into the Trie.

        Args:
            key (str): The word to insert.
            val: Optional value associated with the key (not used in this implementation).
        """
        node = self.root
        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def get_all_words(self):
        """
        Retrieve all words stored in the Trie.

        Returns:
            List[str]: A list of all words in the Trie.
        """
        result = []

        def dfs(node, prefix):
            if node.is_end:
                result.append(prefix)
            for ch, child in node.children.items():
                dfs(child, prefix + ch)

        dfs(self.root, "")
        return result

    def keys_with_prefix(self, prefix):
        """
        Retrieve all words that start with the given prefix.

        Args:
            prefix (str): The prefix to search for.

        Returns:
            List[str]: A list of words starting with the prefix.
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        result = []

        def dfs(n, pre):
            if n.is_end:
                result.append(pre)
            for c, child in n.children.items():
                dfs(child, pre + c)

        dfs(node, prefix)
        return result


class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        """
        Count how many words in the Trie end with the specified suffix pattern.

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
        return count

    def has_prefix(self, prefix) -> bool:
        """
        Check if there exists at least one word in the Trie that starts with the specified prefix.

        Args:
            prefix (str): The prefix string to check.

        Returns:
            bool: True if any word starts with the prefix, False otherwise.

        Raises:
            ValueError: If the input prefix is not a string.
        """
        if not isinstance(prefix, str):
            raise ValueError("Prefix must be a string")

        return bool(self.keys_with_prefix(prefix))
