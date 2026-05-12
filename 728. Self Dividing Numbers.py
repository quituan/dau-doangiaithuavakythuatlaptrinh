class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def is_self_dividing(num):
            temp = num
            while temp > 0:
                digit = temp % 10
                if digit == 0 or num % digit != 0:
                    return False
                temp //= 10
            return True
        result = []
        for n in range(left, right + 1):
            if is_self_dividing(n):
                result.append(n)
        return result