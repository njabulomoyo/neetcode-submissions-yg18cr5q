class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        #{1:2;2:4;4:5}
        res = []
        for key in count:
            if (count[key] * 3) > len(nums):
                res.append(key)
        
        return res











        """
        d = {}

        for elem in nums:
            d[elem] = 1 + d.get(elem,0)
        res=[]
        length = len(nums)
        for key, val in d.items():
            if (val * 3) > length:
                res.append(key)

        return res
        """