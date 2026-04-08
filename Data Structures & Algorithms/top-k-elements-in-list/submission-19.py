class Solution:
    """
    use dictionaries, count occurances and then sort the frequences, then pop from the end
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        freq = [[] for _ in range(len(nums)+1)]

        for key, val in d.items():
            freq[val].append(key)
        res = []
        for i in range(len(freq)-1,-1,-1):
            while freq[i]:
                res.append(freq[i][-1])
                if len(res) == k:
                    return res
                freq[i].pop()






