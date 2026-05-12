class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_single = 0
        sum_double = 0
        for n in nums:
            if n < 10:
                sum_single += n
            else:
                sum_double += n
        return sum_single != sum_double