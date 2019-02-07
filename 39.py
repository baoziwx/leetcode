# 39. Combination Sum
class Solution(object):
    result = []
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # result = []
        self.result = []
        # candidates = sorted(candidates)
        self.findCombinations(candidates, target, [])
        return self.result
#         for n in candidates:
#             if target == n:
#                 result.add([n])

#             result |= combinationSum(candidates, target - n, [])

    def findCombinations(self, candidates, target, prefix):
        # print target, prefix, self.result
        if target < 0:
            return
        elif target == 0:
            # print "yes"
            self.result.append(prefix[:])
        else:
            for i, n in enumerate(candidates):
                prefix.append(n)
                self.findCombinations(candidates[i:], target - n, prefix)
                prefix.pop()
            return
