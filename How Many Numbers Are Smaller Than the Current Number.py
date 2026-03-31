class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)

        rank_map = {}
        for i in range(len(sorted_nums)):
            num = sorted_nums[i]
            if num not in rank_map:
                rank_map[num] = i

        result = []
        for n in nums:
            result.append(rank_map[n])
            
        return result