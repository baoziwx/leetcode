# 787. Cheapest Flights Within K Stops


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        flight_map = {}
        for f in flights:
            i, j, price = f
            # print i, j, price
            if i not in flight_map:
                flight_map[i] = {j: price}
            else:
                flight_map[i][j] = price

        heap = [(0, src, K+1, [src])] # add path
        while heap:
            price, city, stops, path = heapq.heappop(heap)
            if city == dst:
                print path
                return price
            if stops > 0:
                # print city
                # print flight_map[city]
                for d, p in flight_map.get(city, {}).items():
                    heapq.heappush(heap, (price + p, d, stops - 1, path + [d]))
        return -1

