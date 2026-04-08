class Solution:
    """
    "5#hello5#world"
    """
    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res+= str(len(string)) + "#" + string
        return res
            
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            num = ""
            while s[i] != "#":
                num += s[i]
                i+=1
            num = int(num)
            res.append(s[i+1:i+1+num])
            i = i + num + 1

        return res



