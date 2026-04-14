class Solution(object):
    def replaceDigits(self, s):
        chars = list(s)      
        for i in range(1, len(chars), 2):
            prev_char = chars[i-1]
            shift_val = int(chars[i])
            new_char = chr(ord(prev_char) + shift_val)
            chars[i] = new_char
        return "".join(chars)