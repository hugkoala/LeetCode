class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = list()
        for i in range(0, len(nums)):
            num1 = nums[i]
            nums.remove(nums[i])
            for j in range(0, len(nums) - 1):
                num2 = nums[j]
                nums.remove(nums[j])
                if 0 - num1 - num2 in nums:
                    result = [num1, num2, 0 - num1 - num2]
                    result.sort()
                    if result not in results:
                        results.append(result)
                nums.insert(j, num2)
            nums.insert(i, num1)

        return results

