class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # d = {}
        # for idx1, n1 in enumerate(nums):
        #     for idx2, n2 in enumerate(nums):
        #         if idx1 != idx2:
        #             d[n1+n2] = d.get(n1+n2, []) + [[idx1, idx2]]
        # # print d
        # ret = []
        # for idx, n in enumerate(nums):
        #     if -n in d:
        #         for l in d[-n]:
        #             if idx not in l:
        #                 # print d[-n]
        #                 # print idx, n
        #                 # print ''
        #                 entry = sorted([nums[l[0]], nums[l[1]], n])
        #                 if entry not in ret: ret.append(entry)

        nums.sort()
        ret = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            leftIdx = i + 1
            rightIdx = len(nums) - 1

            while leftIdx < rightIdx:
                # print leftIdx, rightIdx
                s = nums[i] + nums[leftIdx] + nums[rightIdx]
                # print 'i = ' + str(i) + ', nums[i] = ' + str(nums[i])
                # print nums[leftIdx]
                # print nums[rightIdx]
                # print s
                # print ''
                if s < 0:
                    leftIdx += 1
                elif s > 0:
                    rightIdx -= 1
                else: #s == 0
                    ret += [[nums[i], nums[leftIdx], nums[rightIdx]]]
                    while leftIdx < rightIdx and nums[leftIdx] == nums[leftIdx + 1]:
                        leftIdx += 1
                        # ret += [[nums[i], nums[leftIdx], nums[rightIdx]]]

                    while leftIdx < rightIdx and nums[rightIdx] == nums[rightIdx - 1]:
                        rightIdx -= 1
                        # ret += [[nums[i], nums[leftIdx], nums[rightIdx]]]

                    leftIdx += 1
                    rightIdx -=1


        return ret
