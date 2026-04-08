from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for string in strs:
            word = [0]*26
            for letter in string:
                word[ord(letter)-ord("a")] += 1
            d[tuple(word)].append(string)

        return d.values()


        