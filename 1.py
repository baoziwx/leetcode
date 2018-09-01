class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for idx, val in enumerate(nums):
            comp = target - val
            if comp in d:
                return [d[comp], idx]
            else:
                d[val] = idx
#         for idx1, val1 in enumerate(nums):
#             for idx2, val2 in enumerate(nums):
#                 if idx1 != idx2 and val1 + val2 == target: return [idx1, idx2]
