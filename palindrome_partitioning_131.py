class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.backtrack(res, [], s, 0)
        return res
    
    def backtrack(self, res, path, s, start):
        if start == len(s):
            res.append([x for x in path])
            return
        for i in range(start, len(s)):
            if self.isPalindrome(s[start:i+1]):
                path.append(s[start:i+1])
                self.backtrack(res, path, s, i+1)
                path.pop()

    def isPalindrome(self, s):
        return s == s[::-1]
