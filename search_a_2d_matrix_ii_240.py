# @author: Zhongyuan Sun
# time: O(log(m*n)), space: O(1)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Solution One: 122ms, beats 50.00%
        # if not matrix or not matrix[0]:
        #     return False
        # m = len(matrix)
        # n = len(matrix[0])
        # i, j = m - 1, 0
        # while i >= 0 and j < n:
        #     if matrix[i][j] > target:
        #         i -= 1
        #     elif matrix[i][j] < target:
        #         j += 1
        #     else:
        #         return True
        # return False
        
        # Solution Two: 216ms, beats 21.36%
        if not matrix or not matrix[0]:
            return False
        for line in matrix:
            if target in line:
                return True
        return False
