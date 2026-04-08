class Solution:
    """
    Edge cases: 
    Solution:
        - initiate dict
        - iterate thru the list
        - for each string, sort
        - check if the sorted string is on the dict
        - if yes, add to the values
        - if no, add to the dictionary
        - return the list of the values


    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for string in strs:
            newStr = tuple(sorted(string))
            d[newStr].append(string)
        return list(d.values())

            









