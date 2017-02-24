class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        frequency_map = {}
        for c in s:
            frequency_map[c] = frequency_map.get(c, 0) + 1
        frequency_map = sorted(frequency_map.items(), lambda x, y: cmp(y[1], x[1]))
        res = ""
        for (x, y) in frequency_map:
            res += x * y
        return res
