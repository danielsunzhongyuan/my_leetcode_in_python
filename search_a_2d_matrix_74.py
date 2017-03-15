# @authro: Zhongyuan Sun
# time: O(log(m*n)), space: O(1)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Solution One
        # if not matrix or not matrix[0]:
        #     return False
        # m = len(matrix)
        # n = len(matrix[0])
        # left, right = 0, m*n-1
        # while left < right:
        #     mid = (left + right) / 2
        #     x = mid / n
        #     y = mid - x*n
        #     if matrix[x][y] < target:
        #         left = mid + 1
        #     elif matrix[x][y] > target:
        #         right = mid
        #     else:
        #         return True
                
        # x = left / n
        # y = left - x * n
        # return target == matrix[x][y]
        
        # Solution Two
        # if not matrix or not matrix[0]: return False
        # for line in matrix:
        #     if target in line:
        #         return True
        # return False
        
        # Solution Three
        return bool(matrix) and target in matrix[bisect.bisect(matrix, [target + 0.5]) - 1]
