class TireNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TireNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TireNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

    def delete(self, word: str) -> None:
        def _delete(curr, word, index):
            # based case at the leaf
            if index == len(word):
                if not curr.end:
                    return False  # word doesn't exist
                curr.end = False
                return len(curr.children) == 0  # if no children, delete this node

            char = word[index]
            if char not in curr.children:
                return False  # word doesn't exist

            should_delete = _delete(curr.children[char], word, index + 1)

            if should_delete:
                # recursively delete
                del curr.children[char]
                return not curr.end and len(curr.children) == 0
            return False

        _delete(self.root, word, 0)


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("apple")
    print(trie.search("app")) # True
    print(trie.search("apple")) # True
    print(trie.search("apples")) # False
    print(trie.startsWith("apples")) # False
    print(trie.startsWith("orange"))  # False
    trie.insert("orange")
    print(trie.startsWith("orange"))  # True
    print(trie.search("orange"))  # True
    trie.delete("apple")
    print(trie.search("app"))  # True
    print(trie.search("apple"))  # False
    print(trie.startsWith("appl"))  # False
