from math import sqrt
class Solution:
    def distance(self,x,y):
        return sqrt((x**2)+(y**2))

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = [[self.distance(elem[0], elem[1]),elem] for elem in points]

        heapq.heapify(res)
        result = []
        for _ in range(k):
            point = heapq.heappop(res)
            result.append(point[1])

        return result
