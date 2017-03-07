# author: Zhongyuan Sun
# Storing the loop numbers will help improving performance from 0.63% to 93.93%

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        x = self.cal(n)
        # loop_numbers = self.all_loop_numbers()
        loop_numbers = [2, 3, 4, 5, 6, 8, 9,
                        11, 12, 14, 15, 16, 17, 18,
                        20, 21, 22, 24, 25, 26, 27, 29,
                        30, 33, 34, 35, 36, 37, 38, 39,
                        40, 41, 42, 43, 45, 46, 47, 48,
                        50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
                        60, 61, 62, 63, 64, 65, 66, 67, 69,
                        71, 72, 73, 74, 75, 76, 77, 78,
                        80, 81, 83, 84, 85, 87, 88, 89,
                        90, 92, 93, 95, 96, 98, 99,
                        106, 113, 117, 128, 145, 162]
        while (x != 1 and x not in loop_numbers):
            x = self.cal(x)
        return x == 1

    def cal(self, n):
        res = 0
        while n:
            res += (n%10)**2
            n /= 10
        return res
        # return sum([int(c)**2 for c in str(n)])

    def all_loop_numbers(self):
        res = []
        for i in range(1, 100):
            tmp = [i]
            next = self.cal(i)
            while next not in res and next not in tmp and next != 1:
                tmp.append(next)
                next = self.cal(next)
            if next != 1:
                res += tmp
            res = list(set(res))
        return res
