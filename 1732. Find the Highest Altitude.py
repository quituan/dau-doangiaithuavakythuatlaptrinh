class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max_height = 0    
        current_height = 0 
        
        for g in gain:
            current_height += g
            if current_height > max_height:
                max_height = current_height
                
        return max_height