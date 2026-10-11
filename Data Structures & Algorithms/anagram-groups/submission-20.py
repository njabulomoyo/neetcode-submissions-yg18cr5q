class Solution:
    """
    output: list of list
    brainstrom:
    - iterate thru the list, check all strings
    - find a way to convert the strs, then check if they belong to a certain anagram
    - store the list, hashset, hashmap
    - add all the anagrams to the list, 
    - return the values of the keys

    edge cases:
    - empty list? no
    - lower english case letters
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            key = self.convertString(string)
            result[key].append(string)

        return list(result.values())


    
    def convertString(self, string):
        var = sorted(string)
        return "".join(var)
        