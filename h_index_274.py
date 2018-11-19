class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        maxCitation, length = max(citations), len(citations)
        if length == 1:
            return min(1, citations[0])
        if maxCitation == 0:
            return 0

        h = 0
        for i in range(1, min(length, maxCitation) + 1):
            if len(filter(lambda x: x >= i, citations)) >= i:
                h = i
        return h
