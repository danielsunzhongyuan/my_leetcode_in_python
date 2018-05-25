class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        def heapify(arr):
            length = len(arr)
            for i in range(length/2, -1, -1):
                heapAdjust(arr, i, length-1)
            
        def heapAdjust(arr, start, end):
            tmp = arr[start]
            j = 2*start
            while j<=end:
                if (j<end and arr[j] > arr[j+1]):
                    j+=1
                if tmp <= arr[j]:
                    break
                arr[start] = arr[j]
                start = j
                j *= 2
            arr[start] = tmp
            
        length = len(nums)
        if length == 0 or length < k:
            return 0
        heap = [num for num in nums[:k]]
        heapify(heap)
        print heap
        for i in range(k, length):
            if nums[i] > heap[0]:
                heap[0] = nums[i]
                heapAdjust(heap, 0, k - 1)
                print heap
        return heap[0]
        

def main():
	s = Solution()
	arr = [3,2,1,5,6,4,10,23,7,9,8,11,34,2,3,4,4,33,33,33,33,2,2,21,123]
	print s.findKthLargest(arr, 10)


if __name__ == "__main__":
	main()
