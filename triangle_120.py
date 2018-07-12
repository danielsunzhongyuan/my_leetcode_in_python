class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Solution One: use O(n**2) space
        # row = len(triangle)
        # if row == 0:
        #     return 0
        # dp = [triangle[row-1]]
        # for i in range(row-1, 0, -1):
        #     dp.insert(0, [0]*i)
        # for i in range(row-2, -1, -1):
        #     tmp = []
        #     for j in range(i+1):
        #         tmp.append(triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1]))
        #     dp[i] = tmp
        # print dp
        # return dp[0][0]

        # Solution Two: use O(n) space
        row = len(triangle)
        if row == 0:
            return 0
        dp = [i for i in triangle[row - 1]]
        for i in range(row - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        print dp
        return dp[0]

if __name__ == "__main__":
    s = Solution()
    print s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])