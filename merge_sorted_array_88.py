class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void DO NOT return anything, modify nums1 in-place instead.
        """
        x = m + n - 1
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[x] = nums1[i]
                x -= 1
                i -= 1
            else:
                nums1[x] = nums2[j]
                x -= 1
                j -= 1
        if i < 0:
            nums1[0:j+1] = nums2[0:j+1]
