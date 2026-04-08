class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for string in strs:
            key = [0]*26
            for letter in string:
                indx = ord("z") - ord(letter)
                key[indx]+=1
            d[tuple(key)].append(string)

        return d.values()

        """
        strs_d = defaultdict(list)

        for string in strs:
            sorted_str = "".join(sorted(string))
            strs_d[sorted_str].append(string)

        return strs_d.values()
        """
            


