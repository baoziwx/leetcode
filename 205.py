class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if len(s) <> len(t):
        #     return False

        l = len(s) #same length
        i = 0
        sTot = {}
        tTos = {}
        while i < l:
            # d[s[i]] = l[i]
            # mapped = l[i]
            if s[i] in sTot or t[i] in tTos:
                if s[i] not in sTot or sTot[s[i]] != t[i]:
                    return False
                if t[i] not in tTos or tTos[t[i]] != s[i]:
                    return False
            else:
                sTot[s[i]] = t[i]
                tTos[t[i]] = s[i]

            i += 1
            # s[i] = replacement
            # if s[:i] != l[:i]: return False

        return True