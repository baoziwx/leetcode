class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        C_indicies = []
        for i in range(len(S)):
            if S[i] == C:
                C_indicies += [i]

        output = []
        for i in range(len(S)):
            # print output
            # print [x - i for x in C_indicies]
            # print map(abs, [x - i for x in C_indicies])
            # print ""
            output += [min(map(abs, [x - i for x in C_indicies]))]

        return output