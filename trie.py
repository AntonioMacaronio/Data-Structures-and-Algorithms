class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        currNode = self.root
        for i, c in enumerate(word):
            if c in currNode.children:
                currNode = currNode.children[c]
            else:
                currNode.children[c] = TrieNode(c)
                currNode = currNode.children[c]
            if i == len(word) - 1:
                currNode.end = True
                
    def remove(self, word):
        currNode = self.root
        nodePath = []
        for i, c in enumerate(word):
            nodePath.append((currNode, currNode.children[c]))
            currNode = currNode.children[c]
        nodePath[-1][1].end = False
        
        for parentOfNode, node in reversed(nodePath):
            if len(node.children) == 0:
                del parentOfNode.children[node.char]
            else:
                return
    
    # returns True if word is inside the Trie
    def search(self, word: str) -> bool:
        currNode = self.root
        for i, c in enumerate(word):
            if c in currNode.children:
                currNode = currNode.children[c]
            else:
                return False
        return currNode.end == True

    # returns True with there is a word starting with prefix
    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for i, c in enumerate(prefix):
            if c in currNode.children:
                currNode = currNode.children[c]
            else:
                return False
        return True

def __main__():
    testTrie = Trie()
    testTrie.insert("hello")
    print(testTrie.search('hello'))
    print(testTrie.startsWith('hel'))

if __name__ == "__main__":
    __main__()