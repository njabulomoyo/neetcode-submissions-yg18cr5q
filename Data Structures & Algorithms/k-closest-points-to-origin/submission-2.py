from math import sqrt
class Solution:
    """
    output: list of list with the coordinates
    find the distance for each coordinate and store it
    then sort the coordinates according to their distance
    then add k closest coordinates to the resulting list
    return the list
    """
    def distance(self, x, y):
        sum = x**2 + y**2
        return sqrt(sum)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [(self.distance(elem[0], elem[1]),elem) for elem in points]
        heapq.heapify(minHeap)

        res = []
        for _ in range(k):
            c = heapq.heappop(minHeap)
            res.append(c[1])

        return res