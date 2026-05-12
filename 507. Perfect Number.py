import math

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        d = 1
        
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                d += i
                if i * i != num:
                    d += num // i
        return d == num