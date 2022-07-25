from tries.trie_node import TrieNode


def test_put():
    node = TrieNode.put(None, 'test', 1, 0)
    p = node
    for c in 'test':
        assert p.children[ord(c)]
        p = p.children[ord(c)]

    assert p.val == 1


def test_get_node():
    node = TrieNode.put(None, 'test', 2, 0)
    target = TrieNode.get_node(node, 'test')
    assert target.val == 2


def test_remove():
    node = TrieNode.put(None, 'test', 3, 0)
    node = TrieNode.put(node, 'that', 4, 0)

    assert TrieNode.get_node(node, 'test').val == 3
    assert TrieNode.get_node(node, 'that').val == 4
