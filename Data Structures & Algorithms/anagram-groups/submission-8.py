class Solution:
    """
    Understand:
    Grouping differnt anagrams together
    input - list
    output - list of list (2d array)
    edge cases:
        - empty list? 
        - there aren't any anagrams?
        - will it only be letters? if so will there be Upper and Lowercase?
        - 
    Match:
     - dictionary 
     - iteration

    Plan:
    1. iterate through the whole list
    2. determine whether an element is an anagram already on the dictionary
    3. if it is, then add the string onto the values of that anagram
    4. otherwise create new key and add the anagram
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_s = defaultdict(list)
        

        for i in strs:
            key = self.convert(i)
            dict_s[key].append(i)

        return dict_s.values()



    def convert(self, string):
        new = [0]*26
        for i in string:
            ind = ord("z") - ord(i)
            new[ind] += 1
        return tuple(new)


    

        