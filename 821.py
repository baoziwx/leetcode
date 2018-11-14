class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
#         C_indicies = []
#         for i in range(len(S)):
#             if S[i] == C:
#                 C_indicies += [i]

#         output = []
#         for i in range(len(S)):
#             # print output
#             # print [x - i for x in C_indicies]
#             # print map(abs, [x - i for x in C_indicies])
#             # print ""
#             output += [min(map(abs, [x - i for x in C_indicies]))]

#         return output



        prev = -1
        l = len(S)
        output = [l]*l
        for i in range(l):
            if S[i] == C:
                prev = i
                output[i] = 0
            elif prev >= 0:
                output[i] = i - prev

        prev = l*2
        for i in range(1, l + 1):
            if S[l-i] == C:
                prev = l-i
            elif prev >= 0:
                output[l-i] = min(output[l-i], prev - (l - i))

        return output



