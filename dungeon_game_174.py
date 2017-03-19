# @question: 174. Dungeon Game
# @author: Zhongyuan Sun
# @time: O(M*N)
# @space: O(M*N)

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]:
            return 1
        m = len(dungeon)
        n = len(dungeon[0])
        least_HP_needed = []
        for i in xrange(m):
            least_HP_needed.append([1] * n)

        least_HP_needed[m-1][n-1] = 1 - dungeon[m-1][n-1] if dungeon[m-1][n-1] < 0 else 1

        # Last row
        for i in xrange(n-2, -1, -1):
            least_HP_needed[m-1][i] = max(1, least_HP_needed[m-1][i+1] - dungeon[m-1][i])
        # Last column
        for i in xrange(m-2, -1, -1):
            least_HP_needed[i][n-1] = max(1, least_HP_needed[i+1][n-1] - dungeon[i][n-1])

        # In the middle
        for i in xrange(m-2, -1, -1):
            for j in xrange(n-2, -1, -1):
                least_HP_needed[i][j] = max(1, min(least_HP_needed[i+1][j], least_HP_needed[i][j+1]) - dungeon[i][j])

        return least_HP_needed[0][0]

