class Solution:
    """
    Solution:
        - arrange the list in descending order
        - if there are two or more values left, pop twice
        - compare the two values
        - if they are equal, contine
        - if not, add the difference of the two back to the list
        - repeat until there is 1 or number left
        - if there is no number left, return 0, otherwise return that number
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-elem for elem in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)      

            if x == y:
                continue
            else:
                diff = abs(x-y)
                heapq.heappush(stones, -diff)  
        if not stones:
            return 0
        return -stones[0]
        