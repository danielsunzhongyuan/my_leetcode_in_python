class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        m = len(matrix)
        if m == 0:
            return ret
        n = len(matrix[0])
        if n == 0:
            return ret
        self.spiralOrderRecursion(matrix, ret, 0, m, 0, n)
        return ret
        
    def spiralOrderRecursion(self, matrix, ret, row_min, row_max, col_min, col_max):
        if row_min >= row_max or col_min >= col_max:
            return

        if row_min<row_max and col_min<col_max:
            for i in range(col_min, col_max):
                ret.append(matrix[row_min][i])
        row_min+=1
        
        if row_min<row_max and col_min<col_max:
            for i in range(row_min, row_max):
                ret.append(matrix[i][col_max-1])
        col_max-=1
        
        if row_min<row_max and col_min<col_max:
            for i in range(col_max-1, col_min-1, -1):
                ret.append(matrix[row_max-1][i])
        row_max -= 1
        
        if row_min<row_max and col_min<col_max:
            for i in range(row_max-1, row_min-1, -1):
                ret.append(matrix[i][col_min])
        col_min += 1
        
        self.spiralOrderRecursion(matrix, ret, row_min, row_max, col_min, col_max)
        

def main():
	s = Solution()
	matrix = [[1,2,3],[4,5,6],[7,8,9]]
	ret = s.spiralOrder(matrix)
	print ret

if __name__ == "__main__":
	main()

