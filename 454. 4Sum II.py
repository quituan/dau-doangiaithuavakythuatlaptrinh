class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        count_map = {}
        ans = 0
        for i in nums1:
            for j in nums2:
                s = i + j
                count_map[s] = count_map.get(s, 0) + 1
        for k in nums3:
            for l in nums4:
                target = -(k + l)
                if target in count_map:
                    ans += count_map[target]
                    
        return ans