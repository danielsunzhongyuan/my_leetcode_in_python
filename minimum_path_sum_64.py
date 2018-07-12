class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        if col == 0:
            return 0
        dp = [[0] * col for _ in range(row)]
        dp[row - 1][col - 1] = grid[row - 1][col - 1]
        for i in range(row - 2, -1, -1):
            dp[i][col - 1] = grid[i][col - 1] + dp[i + 1][col - 1]
        for j in range(col - 2, -1, -1):
            dp[row - 1][j] = grid[row - 1][j] + dp[row - 1][j + 1]
        for i in range(row - 2, -1, -1):
            for j in range(col - 2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]
