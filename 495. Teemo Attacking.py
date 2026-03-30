class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries or duration == 0:
            return 0
            
        total_time = 0
        n = len(timeSeries)
        for i in range(n - 1):
            diff = timeSeries[i+1] - timeSeries[i]
            total_time += min(diff, duration)
        total_time += duration
        
        return total_time