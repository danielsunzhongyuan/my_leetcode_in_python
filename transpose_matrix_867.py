class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(A)
        if row == 0:
            return [[]]
        col = len(A[0])
        if col == 0:
            return [[]]
        ret = [[0]*row for _ in range(col)]
        for i in range(row):
            for j in range(col):
                ret[j][i] = A[i][j]
        return ret
        # return zip(*A)
