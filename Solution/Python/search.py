class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        left = 0
        right = len(nums) - 1

        while True:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right

            middle = (left + right) // 2
            if middle == right or middle == left:
                return -1
            if nums[middle] == target:
                return middle
            if nums[middle] > nums[right]:
                if nums[left] <= target and target <= nums[middle]:
                    right = middle
                else:
                    left = middle + 1
            else:
                if nums[middle] <= target and target <= nums[right]:
                    left = middle
                else:
                    right = middle - 1
