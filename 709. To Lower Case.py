class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        
        for char in s:
            ascii_val = ord(char)

            if 65 <= ascii_val <= 90:
                result += chr(ascii_val + 32)
            else:
                result += char
                
        return result