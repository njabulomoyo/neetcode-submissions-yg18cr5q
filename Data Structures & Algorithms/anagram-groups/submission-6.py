class Solution:
    """
    input - list
    output - list of lists. all anagrams group in their sets.
    edge cases: 
    empty list - 
    will the string have any pther characters? other than letters?
    Match:
    - iteration
    - sorting
    - dictionaries

    Plan:
    1. create the dictionary
    2. iterate through the list
    3. change string to suit the key format
    4. check if it if unique, 
    6. if it exist, add the value onto the existing key
    7. otherwise, create the new key and add the value
    8. return the values of the dictionary

    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_dict = defaultdict(list)
        for i in range(len(strs)):
            anagram = self.convert(strs[i])
            s_dict[anagram].append(strs[i])
        return s_dict.values()

            

    def convert(self,s):
        new = [0]*26
        for i in range(len(s)):
            indx = ord("z") - ord(s[i])
            new[indx] += 1
        return tuple(new)




    
        
