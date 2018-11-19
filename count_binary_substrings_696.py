class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Solution One: use stack will be quite slow
        # if "" == s:
        #     return 0
        # length = len(s)
        # stack1 = []
        # stack2 = []
        # count = 0
        # i = 0
        # for c in s:
        #     if not stack2:
        #         stack2.append(c)
        #     else:
        #         if c == stack2[-1]:
        #             stack2.append(c)
        #         else:
        #             count += min(len(stack1), len(stack2))
        #             stack1[:] = stack2[:]
        #             stack2 = [c]
        # count += min(len(stack1), len(stack2))
        # return count

        # Solution Two: remove stack, only remain the length of stack1 and stack2.
        # also, the pre character, i.e. stack2[-1]
        if "" == s:
            return 0
        len_stack1 = 0
        len_stack2 = 0
        count = 0
        pre = s[0]
        for c in s:
            if c == pre:
                len_stack2 += 1
            else:
                count += min(len_stack1, len_stack2)
                len_stack1 = len_stack2
                len_stack2 = 1
                pre = c
        count += min(len_stack1, len_stack2)
        return count


if __name__ == "__main__":
    a = Solution()
    print a.countBinarySubstrings("00110")
