class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 0
        total = 0
        count = defaultdict(int)
        res = 0
        while r < len(fruits):
            #check the length of dict

            #adding new key to dict
            if len(count) < 3:
                count[fruits[r]] += 1
                total += 1
            
            
            ##removing elems when len(dict) == 2
            if len(count) == 3:
                while l < r and len(count) >2:
                    count[fruits[l]] -= 1
                    total -= 1
                    if count[fruits[l]] == 0:
                        del count[fruits[l]]
                    l += 1
            res = max(res, total)
            r += 1
        return res