class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        for row in matrix:
            if len(set(row)) != n:
                return False
        for c in range(n):
            column = []
            for r in range(n):
                column.append(matrix[r][c])
            if len(set(column)) != n:
                return False
        return True