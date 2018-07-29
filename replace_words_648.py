class Node(object):
    def __init__(self):
        self.text = ""
        self.content = {}
        self.exists = False
        
    def __str__(self):
        return "Text: " + self.text + ", content: " + str(self.content.items()) + ", exists: " + str(self.exists)

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            if c not in cur.content:
                new_node = Node()
                new_node.text = cur.text + c
                cur.content[c] = new_node
            cur = cur.content[c]
        cur.exists = True
        return
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for c in word:
            if cur.exists:
                return True, cur.text
            if c not in cur.content:
                break
            cur = cur.content[c]
        if cur.exists:
            return True, cur.text
        return False, ""


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for word in dict:
            trie.insert(word)
        replace_sentence = sentence.split(" ")
        for i in range(len(replace_sentence)):
            exists, txt = trie.search(replace_sentence[i])
            if exists:
                replace_sentence[i] = txt
        return " ".join(replace_sentence)


if __name__ == "__main__":
    a = Solution()
    dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print a.replaceWords(dict, sentence)
