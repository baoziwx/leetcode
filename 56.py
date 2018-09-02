# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []

        intervals.sort(key=lambda i: i.start)

        for i in intervals:
            if result == [] or result[-1].end < i.start:
                result.append(i)
            else:
                result[-1].end = max(result[-1].end, i.end)

        return result
#         minDict = {}
#         maxDict = {}
#         r = []
#         for i in intervals:
#             for x in range(i.start, i.end):
#                 if not x in minDict:
#                     minDict[x] = i.start
#                 else:
#                     minDict[x] = min(x, minDict[x])

#                 if not x in maxDict:
#                     maxDict[x] = i.end
#                 else:
#                     maxDict[x] = max(x, maxDict[x])

#         print minDict
#         mins = sorted(list(set(minDict.values())))
#         maxs = sorted(list(set(maxDict.values())))
#         for idx, i in enumerate(mins):
#             r.append([i, maxs[idx]])

#         return r
