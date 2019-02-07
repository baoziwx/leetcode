# 336. Palindrome Pairs
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def isPalindrome(w):
            return w == w[::-1]
            # for i in range(len(w) / 2 + 1):
            #     if w[i] != w[-i-1]:
            #         return False
            # return True

        def reverse(w):
            return w[::-1]
        # result = []
        # for i in range(len(words)):
        #     for j in range(len(words)):
        #         if i <> j and isPalindrome(words[i]+words[j]):
        #             result.append([i, j])
        # return result
        result = []
        word_map = {w:i for i, w in enumerate(words)}
        # for w in words:

        for idx, w in enumerate(words):
            if w == "":
                for idx2, w2 in enumerate(words):
                    if isPalindrome(w2) and w <> w2:
                        # print 'a', w2
                        result.append([idx, idx2])
                        result.append([idx2, idx])

            if reverse(w) in word_map:
                r_idx = word_map[reverse(w)]
                if idx <> r_idx:
                    # print 'b'
                    result.append([idx, r_idx])
                # result.append([r_idx, idx])
            # if len(w)
            for i in range(1, len(w)):
                if isPalindrome(w[:i]) and reverse(w[i:]) in word_map:
                    r_idx = word_map[reverse(w[i:])]
                    if r_idx <> idx:
                        # print 'c', w[:i], reverse(w[i:])
                        result.append([r_idx, idx])
                if isPalindrome(w[i:]) and reverse(w[:i]) in word_map:
                    r_idx = word_map[reverse(w[:i])]
                    if r_idx <> idx:
                        # print 'd', w[i:], reverse(w[:i])
                        result.append([idx, r_idx])
        return result