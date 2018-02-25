class Solution(object):
    # 把二维数组分解为 length/2 个同心框，把每个框旋转一下即可
    # 每个框分解为多个组合，每个组合4个点，对应每个点旋转后可能处于的位置
    # 把这4个点按顺时针旋转一下
    # 性能不好！
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length/2):
            self.rotateBorder(matrix, i, length)
        
    def rotateBorder(self, matrix, i, length):
        for j in range(i, length - i - 1):
            self.rotateFourPoints(matrix, i, j, length)
            
    def rotateFourPoints(self, matrix, i, j, length):
        tmp = matrix[i][j]
        matrix[i][j] = matrix[length-j-1][i]
        matrix[length-j-1][i] = matrix[length-i-1][length-j-1]
        matrix[length-i-1][length-j-1] = matrix[j][length-i-1]
        matrix[j][length-i-1] = tmp
