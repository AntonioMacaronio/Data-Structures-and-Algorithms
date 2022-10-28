class Trie:
    class TrieNode():
        def __init__(self):
            self.children = {}
            self.end = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        currNode = self.root
        for i, c in enumerate(word):
            if c in currNode.children:
                currNode = currNode.children[c]
            else:
                nextNode = self.TrieNode()
                currNode.children[c] = nextNode
                currNode = nextNode
            
            if i == len(word) - 1:
                currNode.end = True
        
    def search(self, word: str) -> bool:
        currNode = self.root
        for i, c in enumerate(word):
            if c in currNode.children:
                currNode = currNode.children[c]
            else:
                return False
        return currNode.end == True

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for i, c in enumerate(prefix):
            if c in currNode.children:
                currNode = currNode.children[c]
            else:
                return False
        return True