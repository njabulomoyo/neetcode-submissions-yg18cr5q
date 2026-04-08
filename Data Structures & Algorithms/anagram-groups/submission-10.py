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
        d = defaultdict(list)
        for word in strs:
            new = [0] * 26
            for letter in word:
                new[ord(letter)-ord("a")] += 1
            d[tuple(new)].append(word)

        return list(d.values())
         


