class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def countLess(nums, x):
            ret = 0
            for num in nums:
                if num <= x:
                    ret += 1
            return ret
        
        length = len(nums)
        n = length - 1
        i, j = 1, n
        while i < j:
            mid = (i+j)/2
            x = countLess(nums, mid)
            if x <= mid:
                i = mid+1
            else:
                j = mid
        return i
    

def main():
    s = Solution()
    print s.findDuplicate([1,3,4,2,2])
    print s.findDuplicate([1,3,3,4,2])
    print s.findDuplicate([1,3,5,4,2,5])


if __name__ == "__main__":
    main()
