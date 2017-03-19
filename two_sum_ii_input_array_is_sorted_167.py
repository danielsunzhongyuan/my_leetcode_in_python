class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Solution One: TLE
        # length = len(numbers)
        # for index, number in enumerate(numbers):
        #     for j in range(index+1, length):
        #         if number + numbers[j] == target:
        #             return (index+1, j+1)
        
        # Solution Two: 70ms (Notice line # 19, it's a little optimize of "right = right", because when index is getting larger, the right would be less or equal
        # length = len(numbers)
        # right = length - 1
        # for index, number in enumerate(numbers):
        #     left, right = index+1, right
        #     while left < right:
        #         mid = left + ((right - left)>>1)
        #         if numbers[mid] < target-number:
        #             left = mid + 1
        #         elif numbers[mid] > target-number:
        #             right = mid
        #         else:
        #             return (index+1, mid+1)
        #     if numbers[left] == target-number:
        #         return (index+1, left+1)
        
        # Solution Three: 48ms
        length = len(numbers)
        left, right = 0, length - 1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return (left + 1, right + 1)

