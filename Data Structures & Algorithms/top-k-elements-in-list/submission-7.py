from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        res = []
        #[1,2,2,2,2,3,3]
        for i in nums:
            d[i] += 1 #{1:1,2:3,3:3}
        d2 = defaultdict(list)
        for key, val in d.items():
            d2[val].append(key) #{1:[1],3:[2,3]}
        values = sorted(list(set(d.values())), reverse=True)

        for freq in values:
            res.extend(d2[freq])
            if len(res) >= k:
                return res[:k]
                




        