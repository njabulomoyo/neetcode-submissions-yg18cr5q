class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        
        return res



    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        i=0
        res = []
        while i <len(s):
            new = ""
            while s[i] != "#":
                new += s[i]
                i += 1
            num = int(new)
            l=""
            for j in range(i+1,i+1+num):
                l += s[j]
            res.append(l)
            i = num + i + 1

        return res

        

