class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        limit = len(candyType) // 2

        unique_candies = len(set(candyType))
        return min(unique_candies, limit)