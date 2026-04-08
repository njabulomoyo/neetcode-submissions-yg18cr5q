class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for string in strs:
            lst = [0]*26
            for char in string:
                lst[ord('z') - ord(char)] +=1
            key = tuple(lst)

            d[key].append(string)

        return list(d.values())

            
