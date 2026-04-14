from collections import Counter

class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = Counter(nums)
        total_sum = 0
        for num, frequency in counts.items():
            if frequency == 1:
                total_sum += num
                
        return total_sum