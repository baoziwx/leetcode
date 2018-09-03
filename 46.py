class Solution(object):

    # def __init__(self):
    #     self.result = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # self.result = []
        result = []
        self.permuteSubnums([], nums, result)
        return result


    def permuteSubnums(self, prefix, subNums, result):
        # print 'prefix = '
        # print prefix
        # print 'subNums = '
        # print subNums
        # print 'result = '
        # print self.result
        if subNums == []:
            # self.result.append(prefix)
            # print prefix
            result.append(prefix[:])
        else:
            for idx, n in enumerate(subNums):
#               choose
                prefix.append(n)
                del subNums[idx]

#               explore
                self.permuteSubnums(prefix, subNums, result)

#               unchoose
                subNums.insert(idx, n)
                del prefix[-1]

#         print 'result = '
#         print result
