class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # prev = None
        currLen = maxLen = 0
        prevChars = ''
        for c in s:
            if c in prevChars:
                maxLen = max(maxLen, len(prevChars))
                # currLen = 1
                prevChars = prevChars[prevChars.rindex(c) + 1:]
                # print '1'
                # print prevChars
                # print '1'
#             else:
#                 currLen += 1

            prevChars += c
            # print prevChars

        maxLen = max(maxLen, len(prevChars))

        return maxLen