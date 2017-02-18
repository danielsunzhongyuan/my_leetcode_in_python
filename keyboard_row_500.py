class Solution(object):
    character_map = {"q":2,"w":2,"e":2,"r":2,"t":2,"y":2,"u":2,"i":2,"o":2,"p":2,
    "a":3,"s":3,"d":3,"f":3,"g":3,"h":3,"j":3,"k":3,"l":3,
    "z":5,"x":5,"c":5,"v":5,"b":5,"n":5,"m":5}
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # return filter(self.inOneLine, words)
        # return [word for word in words if self.inOneLine(word)]
        return [word for word in words if len(set([self.character_map[c.lower()] for c in word])) == 1]
        # return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)
        
    def inOneLine(self, word):
        word = word.lower()
        if word:
            tmp = self.character_map[word[0]]
            for c in word:
                if tmp != self.character_map[c]:
                    return False
            return True
        return False
