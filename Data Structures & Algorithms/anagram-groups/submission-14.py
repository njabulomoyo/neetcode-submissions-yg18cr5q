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
    
    + initiate the default dictionary
    + iterate thru the list
    + the initiate the bucket list
    + iterate thru he string
    + add to the dictionary
    + do it till the end of the list
    + return the listvalues

    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for string in strs:
            bucket = [0]*26
            for i in string:
                bucket[ord(i)-ord('z')] += 1
            d[tuple(bucket)].append(string)

        return list(d.values())


            









