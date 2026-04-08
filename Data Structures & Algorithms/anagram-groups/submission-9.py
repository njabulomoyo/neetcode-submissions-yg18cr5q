class Solution:
    """
    input - list of strings
    output - list of lists grouped anagrams
    empty?No
    list with empty string? empty string
    time o(m*n) and space o(m) complexity?
    Upper/lower case? special characters? No
    match:
        hashmap
        list
    plan
    """
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sdic = defaultdict(list)
        for word in strs:
            new = "".join(sorted(word))
            sdic[new].append(word)

        return list(sdic.values())