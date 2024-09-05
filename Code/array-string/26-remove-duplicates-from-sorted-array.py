class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1 or len(nums) > 3*(10**4):
            raise ValueError('Constraint not respected: 1 <= nums.length <= 3 * 10**4')
        if nums != sorted(nums):
            raise ValueError('Constraint not respected: nums is sorted in non-decreasing order.')

        nums_unique = []
        i = 0
        while i < len(nums):
            if len(nums) < -100 or len(nums) > 100:
                raise ValueError('Constraint not respected: -100 <= nums[i] <= 100')
            if nums[i] in nums_unique:
                nums.pop(i)
            else:
                nums_unique.append(nums[i])
                i += 1
        return len(nums)  
        
