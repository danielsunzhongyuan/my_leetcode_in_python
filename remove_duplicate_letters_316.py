class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = [0]*26 # Counters needed
        res = '' # And an answer container
        used = [False]*26 # Some used marks as well 
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        for c in s:
            ci = ord(c) - ord('a')
            cnt[ci] -= 1
            if used[ci]:
                continue
            for j in xrange(len(res)-1, -1, -1): # Checking backward for some dulplicate leters
                cj = ord(res[j]) - ord('a')
                if cj > ci and cnt[cj] > 0:
                    used[cj] = False
                    res = res[:j] + res[j+1:]
                    j -= 1
                else:
                    break
            used[ci] = True
            res += c
        return res
