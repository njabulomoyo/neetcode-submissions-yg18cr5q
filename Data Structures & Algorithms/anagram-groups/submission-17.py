class Solution:
    """
    output - list of lists
    solution:
    
    - create dict
    - iterate thru all strings
    - for each string, create, frequency count arrays
    - iterate thru the string, while updating the array
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for string in strs:
            s = [0]*26
            for char in string:
                s[ord(char) - ord('a')] += 1
            d[tuple(s)].append(string)

        return list(d.values())










