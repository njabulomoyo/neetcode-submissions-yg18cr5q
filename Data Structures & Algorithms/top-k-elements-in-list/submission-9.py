class Solution:
    """
    understand:
    - we want k numbers with the highest frequency
    input - list
    output - list
    edge cases:
        - will k be lees than the number of unique numbers on the list?
        - empty list?
        - 
    Match:
        - dictionary
    Plan:
    1. track frequency of the each element
    2. swap the frequency with the numbers, put all the numbers with the same frequency onto the say place
    3. then sort the keys/ frequencies
    4. starting from the largest frequency, add the values on each list onto the result list untile the len of the result list is equal to k

    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictnums = {}
        for i in range(len(nums)):
            dictnums[nums[i]] = 1 + dictnums.get(nums[i],0)
        freq = defaultdict(list)
        for key, value in dictnums.items():
            freq[value].append(key)

        sorted_keys = sorted(freq.keys())[::-1]
        res = []
        for i in sorted_keys:
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res


