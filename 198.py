class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        robbed = {}
        robbed[-2] = 0
        robbed[-1] = 0
        for i in range(0, len(nums)):
            robbed[i] = max(robbed[i - 1], robbed[i - 2] + nums[i])

        return robbed[len(nums) -1]



