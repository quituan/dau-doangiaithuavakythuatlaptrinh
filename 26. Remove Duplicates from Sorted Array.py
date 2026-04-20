class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        vi_tri_ghi = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[vi_tri_ghi - 1]:
                nums[vi_tri_ghi] = nums[i]
                vi_tri_ghi += 1
        return vi_tri_ghi