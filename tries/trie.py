from tries.trie_set import TrieSet


class Trie:
    def __init__(self):
        self.set = TrieSet()

    def insert(self, word):
        self.set.add(word)

    def search(self, word):
        return word in self.set

    def startsWith(self, prefix):
        return self.set.has_key_with_prefix(prefix)


