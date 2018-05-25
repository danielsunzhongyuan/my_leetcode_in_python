class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import bisect
        length = len(nums)
        if length < 3:
            return False
        increasing_numbers = [nums[0]]
        for i in range(1, length):
            if nums[i] == increasing_numbers[-1]:
                continue
            if nums[i] > increasing_numbers[-1]:
                increasing_numbers.append(nums[i])
                if len(increasing_numbers) == 3:
                    return True
            else:
                loc = bisect.bisect_left(increasing_numbers, nums[i])
                increasing_numbers[loc] = nums[i]
        if len(increasing_numbers) >= 3:
            return True
        print increasing_numbers
        return False


def main():
	s = Solution()
	a = [2, 5, 3, 4, 5]
	print s.increasingTriplet(a)


if __name__ == "__main__":
	main()
