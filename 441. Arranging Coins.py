class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        
        while low <= high:
            mid = low + (high - low) // 2
            coins_needed = mid * (mid + 1) // 2
            
            if coins_needed == n:
                return mid
            elif coins_needed < n:
                low = mid + 1
            else:
                high = mid - 1
                
        return high