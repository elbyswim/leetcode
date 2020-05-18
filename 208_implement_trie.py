class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.trie
        for c in word:
            if c in curr:
                curr = curr[c]
            else:
                curr[c] = {}
                curr = curr[c]
        curr['.'] = None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.trie
        for c in word:
            if c in curr:
                curr = curr[c]
            else:
                return False
        return '.' in curr

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.trie
        for c in prefix:
            if c in curr:
                curr = curr[c]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

obj = Trie()
obj.insert('app')
print(obj.search('apple'))
print(obj.search('app'))
print(obj.startsWith('app'))
obj.insert('apples')
print(obj.search('apple'))
print(obj.search('apples'))
print(obj.search('app'))
print(obj.startsWith('app'))