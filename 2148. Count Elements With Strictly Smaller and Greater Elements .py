class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        min_val = min(nums)
        max_val = max(nums)
        count = 0
        for x in nums:
            if min_val < x < max_val:
                count += 1
                
        return count