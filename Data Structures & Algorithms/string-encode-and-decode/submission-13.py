class Solution:
    """
    ["4#neet","4#code","4#love","3#you"]
    '11#need4#code4#love3#you'
    '4
    """

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            new = str(len(string)) + '#' + string
            res.append(new)
        return ''.join(res)


    #'4#need4#code12#lovelovelove3#you'
    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i < len(s): #i=12
            num = []
            string = ''
            while s[i] != '#': #i = 14
                num.append(s[i]) #[12]
                i+=1
            num = int(''.join(num))#12 
            string = s[i+1:i+1+num] #s[15:27]
            res.append(string)#['need','code',']
            i = i + 1 + num #12

        return res







