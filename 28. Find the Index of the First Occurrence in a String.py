class Solution(object):
    def strStr(self, haystack, needle):
        n = len(haystack)
        m = len(needle)       
        for i in range(n - m + 1):
            current_substring = haystack[i : i + m]
            if current_substring == needle:
                return i
        return -1