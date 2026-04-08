class Solution:
    """
    Understand:
    finding if the letter on the first string,are 
    exactly the same letters on the other string
    - input:
    two string 
    - output:
     boolean
    edge cases:
     if strings len is not equal - return False
     empty strings? return false
     will it only be letter? 
     will the string contain numbers?
     Match:
     - dictionary
     Plan:
     1. count the number of frequencies on of the letters on each string,
     through iteration
     2. compare the two dictionaries
     3. if they are the same return True, other false
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            dict_s[s[i]] = 1 + dict_s.get(s[i],0)
            dict_t[t[i]] = 1 + dict_t.get(t[i],0)
        
        return dict_s == dict_t