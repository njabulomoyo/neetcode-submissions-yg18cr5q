class Solution:
    """
    output: list of list(same anagrams)

    Solution:
    - iterate thru the list of strings
    - initiate dictionary
    - for each string, convert into array sort format
    - check if it exists in the dictionary
    - add string to respective dictionary
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = defaultdict(list)

        for word in strs:
            key = self.ConvertString(word)
            d[key].append(word)

        return list(d.values())

    def ConvertString(self, string):

        new = [0]*26
        for elem in string:
            new[ord(elem)-ord('a')] += 1

        return tuple(new)

