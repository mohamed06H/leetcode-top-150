class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) < 0 or len(nums) > 100:
            raise Exception("Constraint not respected: 0 <= nums.length <= 100")
        
        if val < 0 or val > 100:
            raise Exception("Constraint not respected: 0 <= val <= 100")
        k = len(nums)
        i = 0
        while(i < len(nums)):
            if nums[i] < 0 or nums[i] > 50:
                raise Exception("Constraint not respected: 0 <= nums[i] <= 50")
            if nums[i] == val:
                nums.pop(i)
                k -= 1
            else:
                i += 1
        return k
