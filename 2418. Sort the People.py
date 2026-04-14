class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        combined = zip(heights, names)
        sorted_combined = sorted(combined, key=lambda x: x[0], reverse=True)
        return [person[1] for person in sorted_combined]