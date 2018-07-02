class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def nextTerm(x):
            l = len(x)
            ret = ""
            i = 0
            while i < l:
                tmp_count = 1
                while i+1 < l and x[i+1] == x[i]:
                    tmp_count += 1
                    i += 1
                ret += str(tmp_count) + x[i]
                i += 1
            return ret

        ret = "1"
        for i in range(n-1):
            ret = nextTerm(ret)
        return ret

def main():
    s = Solution()
    s.countAndSay(5)


if __name__ == "__main__":
    main()
