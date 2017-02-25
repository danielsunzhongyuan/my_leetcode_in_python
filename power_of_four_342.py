class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # if num <= 0:
        #     return False
        # while num > 1:
        #     if num % 2 > 0:
        #         return False
        #     num = num >> 1
        #     if num % 2 > 0 or num == 1:
        #         return False
        #     num = num >> 1
        # return True
        
        return (num > 0) and (num&(num-1)==0) and ((num-1)%3==0)
