"""
Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        if not temperatures:
            return []
        stack = []
        days = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            if len(stack) == 0 :
                stack.append((i,temperatures[i]))
            else:
                done = False
                while len(stack) > 0 and not done:
                    if stack[-1][1] < temperatures[i]:
                        dt = stack.pop()
                        days[dt[0]] = i - dt[0]
                    else:
                        done = True
                stack.append((i,temperatures[i]))
        return days
