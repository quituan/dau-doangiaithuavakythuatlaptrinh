class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total_drunk = numBottles
        empty_bottles = numBottles

        while empty_bottles >= numExchange:
            new_bottles = empty_bottles // numExchange
            remaining_empty = empty_bottles % numExchange
            total_drunk += new_bottles
            empty_bottles = new_bottles + remaining_empty
            
        return total_drunk