# 269. Alien Dictionary

# from collections import defaultdict, deque
# class Solution(object):
#     def alienOrder(self, words):
#         # a -> b
#         adj = defaultdict(set)
#         # in-degree
#         deg = {c: 0 for w in words for c in w}
#         for i, w1 in enumerate(words[:-1]):
#             w2 = words[i + 1]
#             for c1, c2 in zip(w1, w2):
#                 if c1 == c2: continue
#                 if c2 not in adj[c1]: deg[c2] += 1
#                 adj[c1].add(c2)
#                 break
#         res = ''
#         # start w 0 indegree nodes
#         q = deque([c for c in deg if not deg[c]])
#         while q:
#             c = q.popleft()
#             res += c
#             for n in adj[c]:
#                 deg[n] -= 1
#                 if not deg[n]: q.append(n)
#         return res if len(res) == len(deg) else ''


from collections import deque

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words or len(words) == 0:
            return words
        if len(words) == 1:
            return words[0]

        graph = {}
        in_degree = {c:0 for w in words for c in w}
        # for w in words:
        #     for i in range(len(w) - 1):
        #         if w[i] <> w[i+1]:
        #             if w[i] not in graph:
        #                 graph[w[i]] = set()
        #             if w[i] not in in_degree:
        #                 in_degree[w[i]] = 0
        #             if w[i+1] not in graph[w[i]]:
        #                 graph[w[i]].add(w[i+1])
        #                 in_degree[w[i+1]] = in_degree.get(w[i+1], 0) + 1
        # print graph
        # print in_degree

        for i in range(len(words) - 1):
            curr = words[i]
            next = words[i + 1]
            for j in range(min(len(curr), len(next))):
                if curr[j] <> next[j]:
#                   add pair to graph for traversal
                    if curr[j] not in graph:
                        graph[curr[j]] = set()
                    if curr[j] not in in_degree:
                        in_degree[curr[j]] = 0
                    if next[j] not in graph[curr[j]]:
                        graph[curr[j]].add(next[j])
                        in_degree[next[j]] = in_degree.get(next[j], 0) + 1
                        # if curr[j] not in in_degree:
                        #     in_degree[curr[j]] = 0
                        # print graph
                        # print in_degree
                    break
        # print graph
        # print in_degree

        visited = set()
        order = ""
        # print graph
        # print in_degree
        to_visit = deque([n for n in in_degree if in_degree[n] == 0])
        while to_visit:
            # print order
            # print in_degree
            # print to_visit

            n = to_visit.popleft()
            visited.add(n)
            order += n

            if n in graph:
                for v in graph[n]:
                    # print order
                    in_degree[v] -= 1
                    # print v
                    # print in_degree[v]
                    if in_degree[v] == 0:
                        to_visit.append(v)

            # print ""


        return order if len(order) == len(in_degree) else ""

