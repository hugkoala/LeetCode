class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = list()
        nums.sort()
        for idx, num in enumerate(nums):
            left_idx = idx + 1
            right_idx = len(nums) - 1

            while left_idx < right_idx:
                sum = nums[idx] + nums[left_idx] + nums[right_idx]
                if sum < 0:
                    left_idx += 1
                elif sum > 0:
                    right_idx -= 1
                else:
                    result = [nums[idx], nums[left_idx], nums[right_idx]]
                    if result not in results:
                        results.append(result)
                    left_idx += 1
                    right_idx -= 1

        return results

