class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for idx, num in enumerate(nums):
            if idx + num > len(nums) - 1:
                return True
        else:
            return False