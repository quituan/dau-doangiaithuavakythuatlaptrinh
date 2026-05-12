class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        d = 0
        temp = x
        
        while temp > 0:
            d += temp % 10
            temp //= 10
        if x % d == 0:
            return d
        else:
            return -1