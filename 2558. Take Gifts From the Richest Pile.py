import heapq
import math

class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            max_val = -heapq.heappop(max_heap)
            new_val = int(math.sqrt(max_val))
            heapq.heappush(max_heap, -new_val)
        return -sum(max_heap)