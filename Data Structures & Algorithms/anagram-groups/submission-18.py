class Solution:
    """
    output: list of lists 
    edge cases: if the list is empty: return empty sublist
    constraints:
        - lower letters of the alphabet
        - len(list) >= 1

    Solution:
     - iterate thru li list
     - initiate result dictionary
     - for each string, initiate bucket (list with len==26, each coresponding to alphabet letters)
     - convert string to bucket form, 
     - check if key exist on dict
     - if true, add string to values
     - else, create new key, add string to values
     - do for all strings
     - return dict.values()
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for word in strs:
            con = self.convertString(word)
            d[tuple(con)].append(word)
        return list(d.values())


    def convertString(self, string):
        if not string:
            return []
        result = [0]*26
        for letter in string:
            result[ord(letter)-ord('a')] += 1
        return result











        