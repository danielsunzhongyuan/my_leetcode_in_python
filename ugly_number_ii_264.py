class Solution(object):
    # Solution 1: 1746ms
    # def nthUglyNumber(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     a = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
    #     if n <= 0:
    #         return 0
    #     elif n <= 10:
    #         return a[n-1]
    #     else:
    #         n -= 11
    #         next_round = a
    #         while True:
    #             next_round = filter(lambda x:x>next_round[-1],map(lambda x:x[0]*x[1],itertools.product(next_round,[2,3,5])))
    #             next_round_supplement = list(set(filter(lambda x:x<next_round[-1] and x not in next_round,map(lambda x:x[0]*x[1],itertools.product(next_round,[2,3,5])))))
    #             tmp = []
    #             while len(tmp) != len(next_round_supplement):
    #                 tmp = next_round_supplement
    #                 next_round_supplement = list(set(filter(lambda x:x<next_round[-1] and x not in next_round,map(lambda x:x[0]*x[1],itertools.product(next_round_supplement,[2,3,5])))))
    #                 next_round_supplement = list(set(next_round_supplement + tmp))
    #             next_round = sorted(list(set(next_round + next_round_supplement)))
    #             if n < len(next_round):
    #                 return next_round[n]
    #             else:
    #                 n -= len(next_round)
                
    # Solution 2: 58ms WINNER
    # ugly_numbers = sorted(2**x * 3**y * 5**z for x in range(32) for y in range(int(1+math.log(2,3)*32)) for z in range(int(1+32*math.log(2,5))))
    # def nthUglyNumber(self, n):
    #     return self.ugly_numbers[n-1]
    
    # Solution 3: 282 ms
    def nthUglyNumber(self, n):
        ugly_numbers = [1]
        p2, p3, p5 = 0, 0, 0
        while len(ugly_numbers) < n:
            ugly2 = ugly_numbers[p2] * 2
            ugly3 = ugly_numbers[p3] * 3
            ugly5 = ugly_numbers[p5] * 5
            next_ugly = min(ugly2, ugly3, ugly5)
            ugly_numbers.append(next_ugly)
            if next_ugly == ugly2: p2 += 1
            if next_ugly == ugly3: p3 += 1
            if next_ugly == ugly5: p5 += 1
        return ugly_numbers[n-1]
