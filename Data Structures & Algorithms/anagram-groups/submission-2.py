class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_d = defaultdict(list)

        for string in strs:
            sorted_str = "".join(sorted(string))
            strs_d[tuple(sorted_str)].append(string)

        return strs_d.values()
            


