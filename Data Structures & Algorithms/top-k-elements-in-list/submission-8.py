class Solution:
    """
    understand:
    - input: list
    - output: list containg the most frequent elements
    edge case: 
    empty list?
    can k be more than the number of unique elements on the list?
    Match:
    - dictionary
    - iteration
    planning
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for i in nums:
            dict1[i] = 1 + dict1.get(i,0)
        #{1:1,2:2,3:3,4:2,7:3,9:3}
        dict2 = defaultdict(list)
        for key, val in dict1.items():
            dict2[val].append(key)
        #{}
        sorted_freq = sorted(dict2.keys())[::-1]
        print(sorted_freq)
        #[3,2,1]
        result = []
        for ind in sorted_freq:            
            for j in dict2[ind]:
                result.append(j)
                if len(result) == k:
                    return result


        