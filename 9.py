class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        if x % 10 == 0 and x <> 0: return False

        revertedx = 0
        while x > revertedx:
            revertedx = revertedx * 10 + x % 10
            x /= 10
            # print x
            # print revertedx

        return x == revertedx or x == revertedx / 10