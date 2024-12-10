class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last = nums[len(nums)-k:len(nums)]
        first = nums[:len(nums)-k]
        
        nums[:len(last)] = last
        nums[len(last):len(nums)] = first
       

        # Solution 2: rotate one step to the right k times
        # for i in range(k):
        #     last = nums[len(nums)-1]
        #     nums[1:len(nums)] = nums[0:len(nums)-1]
        #     nums[0] = last
