class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        result = list()
        leftIdx = 0
        rightIdx = len(nums) - 1

        if len(nums) == 0:
            return [-1, -1]
        if nums[0] > target or nums[len(nums) - 1] < target:
            return [-1, -1]
        if leftIdx == rightIdx:
            result.append(leftIdx)
            result.append(rightIdx)



        while leftIdx != rightIdx:
            midIdx = (leftIdx + rightIdx) // 2

            if nums[midIdx] >= target:
                rightIdx = midIdx
            else:
                leftIdx = midIdx + 1

            if rightIdx == leftIdx:
                if nums[leftIdx] == target:
                    result.append(leftIdx)
                else:
                    result.append(-1)

        leftIdx = 0
        rightIdx = len(nums) - 1
        while leftIdx != rightIdx:
            midIdx = (leftIdx + rightIdx) // 2

            if nums[midIdx] > target:
                rightIdx = midIdx
            else:
                leftIdx = midIdx + 1

            if rightIdx == leftIdx:
                if nums[rightIdx] == target:
                    result.append(rightIdx)
                elif nums[rightIdx - 1] == target:
                    result.append(rightIdx - 1)
                else:
                    result.append(-1)

        return result



