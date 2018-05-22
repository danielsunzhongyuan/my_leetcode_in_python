
class Solution(object):
	def generateMatrix(self, n):
		"""
		:type n: int
		:rtype: List[List[int]]
		"""
		ret = [[0]*n for i in range(n)]
		self.generateMatrixRecursion(ret, 0, n, 0, n, 1)
		return ret

	def generateMatrixRecursion(self, matrix, row_min, row_max, col_min, col_max, begin):
		if row_min >= row_max or col_min >= col_max:
			return

		if row_min<row_max and col_min<col_max:
			for i in range(col_min, col_max):
				matrix[row_min][i] = begin
				begin += 1
		row_min += 1

		if row_min<row_max and col_min<col_max:
			for i in range(row_min, row_max):
				matrix[i][col_max-1] = begin
				begin += 1
		col_max -= 1

		if row_min<row_max and col_min<col_max:
			for i in range(col_max-1, col_min-1, -1):
				matrix[row_max-1][i] = begin
				begin += 1
		row_max -= 1

		if row_min<row_max and col_min<col_max:
			for i in range(row_max-1,row_min-1,-1):
				matrix[i][col_min] = begin
				begin += 1
		col_min += 1

		self.generateMatrixRecursion(matrix, row_min, row_max, col_min, col_max, begin)


def main():
	s = Solution()
	ret = s.generateMatrix(3)
	print ret


if __name__ == "__main__":
	main()
