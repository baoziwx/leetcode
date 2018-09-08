class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < - 2**31 or x > (2**31 - 1): return 0

        reversedx = 0
        isNegative = False
        if x < 0:
            isNegative = True
            x = -x

        while x > 0:
            reversedx = 10*reversedx + x % 10
            x /= 10
            if x > 0 and reversedx > 2**31 / 10: return 0 #overflow

        return reversedx if not isNegative else -reversedx
        # return ret if -2**31 < ret < 2**31 - 1 else 0