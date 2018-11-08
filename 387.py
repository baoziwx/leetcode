class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        l = len(s)
        for i in range(l):
            if s[i] in d:
                # d.pop(s[i])
                d[s[i]] = l
            else:
                d[s[i]] = i

        # print d

        # if len(d) == 0:
        #     return -1

        min_idx = l
        for c, i in d.items():
            min_idx = min(min_idx, i)

        return -1 if min_idx == l else min_idx

