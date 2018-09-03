class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        print n
        print x
        if n == 0: return 1.0

        half = 0
        if n < 0:
            x = 1/x
            half = self.myPow(x, -((n + 1) / 2))
            # return half*half if n % 2 == 0 else half*half*x
        else:
            half = self.myPow(x, n/2)

        print half
        return half*half if n % 2 == 0 else half*half*x



