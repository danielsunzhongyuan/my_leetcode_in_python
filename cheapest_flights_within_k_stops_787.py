"""
There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.
Now given all the cities and fights, together with starting city src and the destination dst, 
your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Note:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
"""


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
        costWithKStops = [10000000] * n
        costWithKStops[src] = 0
        preRound = costWithKStops[:]

        i = 0
        nextCities = [src]
        while i <= K:
            tmpForNextCities = []
            for city in nextCities:
                nextStop = self.getDestCityesFromSrc(flights, city)
                for stop in nextStop:
                    costWithKStops[stop[0]] = min(stop[1] + costWithKStops[city], costWithKStops[stop[0]])
                    tmpForNextCities.append(stop[0])
            nextCities = list(set(tmpForNextCities))
            if preRound == costWithKStops:
                break
            preRound = costWithKStops[:]
            print preRound
            i += 1
        return costWithKStops[dst] if costWithKStops[dst] < 10000000 else -1

    def getDestCityesFromSrc(self, flights, src):
        results = []
        for flight in flights:
            if src == flight[0]:
                results.append([flight[1], flight[2]])
        return results


if __name__ == "__main__":
    a = Solution()
    print a.findCheapestPrice(4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1)
