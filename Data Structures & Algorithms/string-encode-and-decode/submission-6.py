class Solution:
    """
    converting a list with strings to a one string, 
    that can be converted back to the original list
    without any change in the strings of the list
    understand: 
    input - list of strings
    output - string
    edge cases:
    - will the strings be letters only?
    - will there be any special characters?
    - empty strings?
    - contains UTF-8 characters

    match:
        -strings
    Plan:
    1. create new string 
    2. iterate through the whole list
    3. for every string we add, we will add the hash symbol
    and the lenght of the string (to remember when we are converting back to the list)
    4. continue till the end ]
    
    2nd part:
    1. have a pointer
    1.2 go through the whole string
    2. when you encounter the hash symbol, skip, the the next character 
    should be converted to a number and used in a loop
    3. the loop will go through the string till the end of the loop to come o=up with the 
    string to be added to the list
    4. do this till the end of the string 
    
    """

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""

        new = ""
        for string in strs:
            new += str(len(string)) + "#" + string

        return new
    #"4#neet4#code4#love3#you"
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        p = 0
        res = []        
        while p < len(s):
            num = ""
            while s[p] != '#':
                num += s[p]
                p+=1
            num = int(num)
            string = ""
            for i in range(p+1, p + 1 + num):
                string += s[i]
            res.append(string)
            p += 1 + num 
        return res





