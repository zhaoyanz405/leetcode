from tries.trie_map import TrieMap


class TrieSet:
    def __init__(self):
        self.trie_map = TrieMap()

    def add(self, k):
        self.trie_map.put(k, 1)

    def remove(self, k):
        self.trie_map.remove(k)

    def __contains__(self, k):
        return k in self.trie_map

    def shortest_prefix_of(self, query):
        return self.trie_map.shortest_prefix_of(query)

    def longest_prefix_of(self, query):
        return self.trie_map.longest_prefix_of(query)

    def keys_with_prefix(self, prefix):
        return self.trie_map.keys_with_prefix(prefix)

    def has_key_with_prefix(self, prefix):
        return self.trie_map.has_key_with_prefix(prefix)

    def keys_with_pattern(self, pattern):
        return self.keys_with_pattern(pattern)

    def has_key_with_pattern(self, pattern):
        return self.has_key_with_prefix(pattern)

    def size(self):
        return self.trie_map.size()
