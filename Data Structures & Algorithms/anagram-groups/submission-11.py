class Solution:
    """
    understanding:
    input - list
    output - list of lists
    any special characters? 
    empty list? []
    Plan:
    0.5 create a list hashmap
    1. create a list for each string:
    2. update the values of the indices that correcpond to letters
    3. change list to tuple to be a key for hashmap
    4. add string to respective matching key
    5. return values of hashmap
    """
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for word in strs:
            lst = [0] * 26
            for letter in word:
                lst[ord("z") - ord(letter)] += 1

            d[tuple(lst)].append(word)

        return list(d.values())











