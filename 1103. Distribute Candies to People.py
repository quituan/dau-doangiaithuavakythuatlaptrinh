class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        ans = [0] * num_people        
        give = 1  
        idx = 0  
        
        while candies > 0:
            actual_give = min(give, candies)

            ans[idx] += actual_give
            candies -= actual_give
            give += 1
            idx = (idx + 1) % num_people
            
        return ans