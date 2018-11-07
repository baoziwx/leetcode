class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s_len = len(s)
        result = []
        if len(s) < 4 or len(s) > 12:
            return []
#       choose
        is_invalid = False
        for i in range(1, 4):
            # print "i = ", i
            for j in range(i+1, i+4):
                # print "j = ", j
                for k in range(j+1, j+4):
                    # print "k = ", k
                    for l in range(k+1, k+4):
                        # print "l = ", l
                        if l == s_len:
                            # print s_len
                            # continue
                            if self.isValidPart(s[:i]) and self.isValidPart(s[i:j]) and self.isValidPart(s[j:k]) and self.isValidPart(s[k:l]):
                                result.append(s[:i] + '.' + s[i:j] + '.' + s[j:k] + '.' + s[k:l])
        return result

    def isValidPart(self, s):
        return 0 < len(s) <= 3 and int(s) <= 255 and (len(s) == 1 or int(s[0]) != 0)

