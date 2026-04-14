class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        digits = number.replace(" ", "").replace("-", "")
        
        results = []
        i = 0
        n = len(digits)

        while n - i > 4:
            results.append(digits[i:i+3])
            i += 3
        remaining = n - i
        
        if remaining == 4:
            results.append(digits[i:i+2])
            results.append(digits[i+2:i+4])
        else:
            results.append(digits[i:])
        return "-".join(results)