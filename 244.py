class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.d = {}
        for idx, word in enumerate(words):
            self.d[word] = self.d.get(word, []) + [idx]


    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return min(abs(i - j) for i in self.d[word1] for j in self.d[word2])



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)