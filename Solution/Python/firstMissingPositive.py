class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for idx in range(0, len(nums)):
            if nums[idx] > 0 and nums[idx] <= len(nums) and nums[idx] != idx + 1:
                temp = nums[nums[idx] - 1]
                nums[nums[idx] - 1] = nums[idx]
                nums[idx] = temp

        for idx, num in enumerate(nums):
            if idx != num - 1:
                return idx + 1
        else:
            return len(nums) + 1