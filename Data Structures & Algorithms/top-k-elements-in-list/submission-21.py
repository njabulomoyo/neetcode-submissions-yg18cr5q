class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numsDict = Counter(nums)
        freq = defaultdict(list)
        for key, val in numsDict.items():
            freq[val].append(key)
        
        freqlist = sorted(list(freq.keys()),reverse=True)
        res = []
        for num in freqlist:
            while freq[num]:
                res.append(freq[num].pop())
                if len(res) == k:
                    return res


