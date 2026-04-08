class Solution:
    """
    understand:
    input - list
    output - list
    edge cases? empty list? return ""
    time and space complexity?
     3*you"
    plan:
        1. 
    """

    def encode(self, strs: List[str]) -> str:
        s= ""
        for i in strs:
            s += str(len(i)) + "*" + i
        return s
    #"4*neet4*code4*love
    def decode(self, s: str) -> List[str]:
        res = []
        j = 0
        while j < (len(s)):
            num = ""
            while s[j] != "*":
                num += s[j] #"4"
                j += 1 #i= 2
            #12
            num = int(num) #4
            temp = ""
                          #(1+1, 6)
            for k in range(j+1, j+1+num):
                temp += s[k]
                #neet            
            j = 1 + j + num

            res.append(temp)
        
        return res







