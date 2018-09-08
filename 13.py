class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        d['I'] = 1
        d['V'] = 5
        d['X'] = 10
        d['L'] = 50
        d['C'] = 100
        d['D'] = 500
        d['M'] = 1000
        d['IV'] = 4
        d['IX'] = 9
        d['XL'] = 40
        d['XC'] = 90
        d['CD'] = 400
        d['CM'] = 900

        i = 0
        r = 0
        while i <= len(s) - 1:
            # print i
            if i == len(s): #at last digit
                r += d[s[i]]
                break
            else:
                if s[i:i+2] in d: # 4, 9, etc
                    r += d[s[i:i+2]]
                    i += 2
                else:
                    r += d[s[i]]
                    i += 1
            # print i

        return r
