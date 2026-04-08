class Solution:
    """
    output - list of lists
    solution:
    bruteforce:
    create dict
    iterate thru all strings
    for each string, sort string
    check if the sorted string is a dict key, if yess add string the other values
    if false, create new key and add string
    do this for all strings
    return the value of the dict
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for string in strs:
            new = "".join(sorted(string))
            d[new].append(string)

        return list(d.values())









