class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        prev = nums[0]
        numsLen = len(nums)
        i = 1
        while i < numsLen:
            print i
            if nums[i] == prev:
                del nums[i]
                numsLen -= 1
            else:
                prev = nums[i]
                i += 1

        return numsLen

#         rewrite in exisiting indexes

