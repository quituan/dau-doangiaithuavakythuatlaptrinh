class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        def merge(left, right):
            sorted_arr = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sorted_arr.append(left[i])
                    i += 1
                else:
                    sorted_arr.append(right[j])
                    j += 1
            sorted_arr.extend(left[i:])
            sorted_arr.extend(right[j:])
            return sorted_arr
        def divide(arr):
            if len(arr) <= 1:
                return arr           
            mid = len(arr) // 2
            left_half = divide(arr[:mid])
            right_half = divide(arr[mid:])
            
            return merge(left_half, right_half)
        return divide(nums)