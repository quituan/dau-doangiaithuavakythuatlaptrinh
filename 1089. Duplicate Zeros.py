class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        zeros = 0
        n = len(arr) - 1

        i = 0
        while i <= n - zeros:
            if arr[i] == 0:
                if i == n - zeros:
                    arr[n] = 0 
                    n -= 1
                    break
                zeros += 1
            i += 1
        last = n - zeros
        for j in range(last, -1, -1):
            if arr[j] == 0:
                arr[j + zeros] = 0
                zeros -= 1
                arr[j + zeros] = 0
            else:
                arr[j + zeros] = arr[j]