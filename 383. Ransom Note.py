from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count_mag = Counter(magazine)
        for char in ransomNote:
            if count_mag[char] <= 0:
                return False
            count_mag[char] -= 1
            
        return True