# 482. License Key Formatting

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-', '')
        l = len(S)
        if l == 0:
            return ''
        result = ''
        begin = end = 0
        if l % K > 0:
            end = l % K
        else:
            end = K
            # result += S[:(l % K) + 1]

        while end <= len(S):
            # print begin, end
            result += S[begin:end].upper() + '-'
            begin = min(begin+K, end)
            # begin += K
            end = begin + K

        return result[:-1]
