class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s=set()
        for i in range(len(nums1)):
            if (nums1[i] in nums2) and (nums1[i] not in s):
                s.add(nums1[i])
        return list(s)