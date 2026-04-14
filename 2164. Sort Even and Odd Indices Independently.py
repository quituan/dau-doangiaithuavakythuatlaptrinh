class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even_indices = sorted(nums[::2])    
        odd_indices = sorted(nums[1::2], reverse=True) 
        
        res = []
        for i in range(len(even_indices)):
            res.append(even_indices[i])
            if i < len(odd_indices):
                res.append(odd_indices[i])
        return res