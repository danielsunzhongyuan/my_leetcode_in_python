class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # length = len(letters)
        # left, right = 0, length - 1
        # while left < right:
        #     mid = (left+right) / 2
        #     print left, mid, right
        #     if letters[mid] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # if letters[left] <= target:
        #     return letters[(left+1)%length]
        # return letters[left]

        import bisect
        idx = bisect.bisect_right(letters, target)
        return letters[idx % len(letters)]


def main():
    s = Solution()
    letters = ['c', 'f', 'j']
    target = 'z'
    print s.nextGreatestLetter(letters, target)


if __name__ == "__main__":
    main()
