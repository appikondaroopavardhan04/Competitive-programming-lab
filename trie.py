
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


def insert(root, word):
    node = root
    for ch in word:
        if ch not in node.children:
            node.children[ch] = TrieNode()
        node = node.children[ch]
    node.is_end = True


def search(root, word):
    node = root
    for ch in word:
        if ch not in node.children:
            return 0
        node = node.children[ch]
    return 1 if node.is_end else 0


n = int(input())
words = input().strip().split(',')
target = input().strip()

root = TrieNode()

for word in words:
    insert(root, word)

print(search(root, target))
