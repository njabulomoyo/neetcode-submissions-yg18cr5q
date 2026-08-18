class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        result = []
        for word in strs:
            result.append(str(len(word)) + "#" + word)

        return "".join(result)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        result = []
        i=0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            print(s[i:j])
            num = int(s[i:j])

            result.append(s[j+1:j+num+1])

            i = j + num + 1

        return result



            
