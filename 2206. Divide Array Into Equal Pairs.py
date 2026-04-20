class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counts = {}
        for x in nums:
            counts[x] = counts.get(x, 0) + 1
            
        for count in counts.values():
            if count % 2 != 0:
                return False
        return True