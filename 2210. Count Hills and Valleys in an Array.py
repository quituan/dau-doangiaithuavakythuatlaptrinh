class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_nums = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                unique_nums.append(nums[i])
        
        count = 0
        for i in range(1, len(unique_nums) - 1):
            if unique_nums[i] > unique_nums[i-1] and unique_nums[i] > unique_nums[i+1]:
                count += 1
            elif unique_nums[i] < unique_nums[i-1] and unique_nums[i] < unique_nums[i+1]:
                count += 1
        return count