class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if s == s[::-1]:
            return s
        ret = ""
        i = 0
        for j in range(i + len(ret) + 1, length + 1):
            if s[:j] == s[j - 1::-1]:
                ret = s[:j]
        for i in range(1, length):
            for j in range(i + len(ret) + 1, length + 1):
                if s[i:j] == s[j - 1:i - 1:-1] and len(ret) < (j - i):
                    ret = s[i:j]
        return ret


def main():
    s = Solution()
    strings = [
        "babad",
        "cbbd",
        "a",
        "bb",
        "abb",
        "bbd",
    ]
    for i in strings:
        print i, s.longestPalindrome(i)


if __name__ == "__main__":
    main()
