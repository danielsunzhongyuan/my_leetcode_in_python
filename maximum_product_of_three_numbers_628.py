class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest_three = [-1003,-1002,-1001]
        smallest_three = [1003,1002,1001]
        
        for i in nums:
            if i > largest_three[0]:
                largest_three[0] = i
                if largest_three[0] > largest_three[1]:
                    largest_three[0], largest_three[1] = largest_three[1], largest_three[0]
                    if largest_three[1] > largest_three[2]:
                        largest_three[1], largest_three[2] = largest_three[2], largest_three[1]
            if i < smallest_three[0]:
                smallest_three[0] = i
                if smallest_three[0] < smallest_three[1]:
                    smallest_three[0], smallest_three[1] = smallest_three[1], smallest_three[0]
                    if smallest_three[1] < smallest_three[2]:
                        smallest_three[1], smallest_three[2] = smallest_three[2], smallest_three[1]
                
        return max([
            largest_three[0]*largest_three[1]*largest_three[2],
            largest_three[2]*smallest_three[1]*smallest_three[2]
        ])
