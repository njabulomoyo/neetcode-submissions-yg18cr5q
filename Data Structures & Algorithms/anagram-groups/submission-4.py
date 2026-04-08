from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for elem in strs:
            string = tuple(sorted(elem))
            d[string].append(elem)

        return d.values()


        