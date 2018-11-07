from heapq import heappush, heappop
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordLen = len(beginWord)

        # preprocess
        d = {}
        for w in wordList:
            for i in range(wordLen):
                s = w[:i] + '_' + w[i+1:]
                d[s] = d.get(s, []) + [w]

        pathLen = 1
        todo = [(pathLen, beginWord)]

        visited = set()

        while todo != []:
            curr = heappop(todo)
            currWord = curr[1]
            pathLen = curr[0]
            if currWord in visited:
                continue

            visited.add(currWord)
            # print visited
            if currWord == endWord: return pathLen

            for i in range(wordLen):
                s = currWord[:i] + '_' + currWord[i+1:]

                if s in d:
                    for neighbor in d[s]:
                        if neighbor not in visited:
                            heappush(todo, (pathLen + 1, neighbor))


        return 0





