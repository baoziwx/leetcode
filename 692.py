from heapq import heappush, heappop
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq_dict = {}
        for w in words:
            freq_dict[w] = freq_dict.get(w, 0) + 1

        freq_heap = []
        for w, f in freq_dict.items():
            heappush(freq_heap, (-f, w))

#         print freq_heap
        out = []
#         l = len(freq_heap)
#         for i in range(l):

#             f, word = heappop(freq_heap)
#             print f, word
#             if i >= l - k:
#                 # print i, len(freq_heap), k
#                 out = [word] + out
        for i in range(k) :
            f, w = heappop(freq_heap)
            out += [w]
        return out