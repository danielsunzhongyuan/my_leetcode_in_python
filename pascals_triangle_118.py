class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Solution 1: 489ms
        # if numRows == 0:
        #     return []
        # elif numRows == 1:
        #     return [[1]]
        # elif numRows == 2:
        #     return [[1],[1,1]]
        # else:
        #     res = [[1],[1,1]]
        #     for i in range(2, numRows):
        #         res.append([1])
        #         for j in range(1, i):
        #             res[i].append(res[i-1][j-1] + res[i-1][j])
        #             print res
        #         res[i].append(1)
        #     return res
        
        # Solution 2: 49ms
        if numRows == 0:
            return []
        else:
            res = []
            for i in range(numRows):
                res.append([1])
                for j in range(1, i+1):
                    res[i].append(self.cal(i,j))
            return res
            
    def cal(self, i, j):
        def factorial(x):
            if x <= 1:
                return 1
            else:
                res = 1
                while x > 1:
                    res *= x
                    x -= 1
                return res
        return factorial(i) / factorial(j) / factorial(i-j)
