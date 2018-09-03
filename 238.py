class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        r = [1]*n

        productFromStart = 1
        for i in range(1, n):
            productFromStart *= nums[i - 1]
            r[i] = productFromStart

        productFromEnd = 1
        for i in range(n-2, -1, -1):
            productFromEnd *= nums[i + 1]
            r[i] *= productFromEnd
        print r

        return r