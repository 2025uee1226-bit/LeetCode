class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p=[]
        for i in range(m):
            p.append(nums1[i])
        for j in range(n):
            p.append(nums2[j])
        p.sort()
        for z in range(len(p)):
            nums1[z]=p[z]
        return nums1
        