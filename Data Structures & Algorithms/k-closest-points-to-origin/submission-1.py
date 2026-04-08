class Solution:
    """
    - calculate the distance from the origin
    - stores the distance in a list
    - negate distance when storing them
    - heapify the list
    - pop k times
    - return the number on top of the heap

    """
    from math import sqrt
    def distance(self,x,y):
        return self.sqrt((x**2) + (y**2))
        

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        maxHeap = [[self.distance(cod[0],cod[1]),cod] for cod in points]
        heapq.heapify(maxHeap)

        for _ in range(k):
            elem = heapq.heappop(maxHeap)
            res.append(elem[1])

        return res





