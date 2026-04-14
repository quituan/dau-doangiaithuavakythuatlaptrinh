from collections import Counter
class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counts = Counter(s)
        frequencies = counts.values()
        return len(set(frequencies)) == 1