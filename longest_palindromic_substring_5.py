class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length < 2 or s == s[::-1]:
            return s
        ret = ""
        for i in range(length):
            for j in range(i + len(ret) + 1, length + 1):
                if s[i:j] == s[j - length - 1:i - length - 1:-1]:
                    ret = s[i:j]
        return ret

        # if len(s) < 2 or s == s[::-1]:
        #     return s
        # n = len(s)
        # start, maxlen = 0, 1
        # for i in range(n):
        #     odd = s[i - maxlen - 1:i + 1]  # len(odd)=maxlen+2
        #     even = s[i - maxlen:i + 1]  # len(even)=maxlen+1
        #     if i - maxlen - 1 >= 0 and odd == odd[::-1]:
        #         start = i - maxlen - 1
        #         maxlen += 2
        #         continue
        #     if i - maxlen >= 0 and even == even[::-1]:
        #         start = i - maxlen
        #         maxlen += 1
        # return s[start:start + maxlen]


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
