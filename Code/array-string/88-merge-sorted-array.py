class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) != m+n:
            raise ValueError('Constraint not respected: nums1.length == m + n')
        if len(nums2) != n:
            raise ValueError('Constraint not respected: nums2.length == n')
        if m < 0 or m > 200:
            raise ValueError('Constraint not respected: 0 <= m, n <= 200')
        if m+n < 1 or m+n > 200:
            raise ValueError('Constraint not respected: 1 <= m + n <= 200')
        
        for i in range(n):
            nums1[m+i] = nums2[i]
        return nums1.sort()
