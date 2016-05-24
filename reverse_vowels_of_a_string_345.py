class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length < 2:
            return s
        i, j = 0, length - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        res = ["a"] * length
        while i <= j:
            while i <= j and s[i] not in vowels:
                res[i] = s[i]
                i += 1
            while i <= j and s[j] not in vowels:
                res[j] = s[j]
                j -= 1
            if i <= j:
                res[i] = s[j]
                res[j] = s[i]
                i += 1
                j -= 1
        return "".join(res)