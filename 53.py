class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentLargestSum = nums[0]
        prevSum = nums[0]

        for idx, val in enumerate(nums):
            if idx == 0: continue
            currentSum = max(prevSum + val, val)
            currentLargestSum = max(currentLargestSum, currentSum)
            prevSum = currentSum

        return currentLargestSum