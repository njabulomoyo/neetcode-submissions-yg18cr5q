class Solution:
    """
    output: list of int
    edge cases: same elements, all uniqie elemets

    solution:
    - create a bucket sort solution
    - create a list of list of len(list)
    - then create dict with count of the unique elements and their freq
    - then from the top/end, start popping from list that are non-empty and appending to the result list
    -return result list
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)

        numlist = [[] for _ in range(len(nums)+1)]

        for key, val in d.items():
            numlist[val].append(key)

        result = []

        for i in range(len(numlist)-1, -1, -1):
            while numlist[i]:
                result.append(numlist[i].pop())
                if len(result) == k:
                    return result










        