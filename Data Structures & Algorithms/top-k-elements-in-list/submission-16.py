class Solution:
    """
    use dictionaries, count occurances and then sort the frequences, then pop from the end
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        new = defaultdict(list)
        #[1:1;2:2;3:3]
        for key, val in d.items():
            new[val].append(key)
        lst = sorted(list(new.keys()),reverse=True)

        res = []
        for num in lst:
            while new[num]:
                res.append(new[num][-1])                
                if len(res) == k:
                    return res
                new[num].pop()



