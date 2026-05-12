class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        min1 = float('inf')
        min2 = float('inf')
        
        for p in prices:
            if p < min1:
                min2 = min1
                min1 = p
            elif p < min2:
                min2 = p
        min_cost = min1 + min2
        if min_cost <= money:
            return money - min_cost
        else:
            return money