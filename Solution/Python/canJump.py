class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_len = 0
        
        for idx, num in enumerate(nums):
            if max_len < idx:
                return False
            if idx + num > max_len:
                max_len = idx + num
                
            if max_len >= len(nums) - 1:
                return True
        else:
            return False