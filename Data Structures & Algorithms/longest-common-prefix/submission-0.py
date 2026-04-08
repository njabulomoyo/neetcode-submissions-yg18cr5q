class Solution:
    """
    understand:
    input - list of strings
    output - string of common preflix
    what is a preflix?
    lower case letters
    expected time and space?
    PLAN:
    1. got through all strings
    2. check string on the corresponding indices, simultaniously
    3. keep track of the strings that are the same 
    4. if string not equal to string in other word, return the stored string 
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or strs[0][i] != word[i]:
                    return res
                
            res+= strs[0][i]

        return res


