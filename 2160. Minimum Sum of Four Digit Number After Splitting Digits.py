class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = sorted(str(num))
        
        new1 = int(digits[0]) * 10 + int(digits[2])
        new2 = int(digits[1]) * 10 + int(digits[3])
        return new1 + new2