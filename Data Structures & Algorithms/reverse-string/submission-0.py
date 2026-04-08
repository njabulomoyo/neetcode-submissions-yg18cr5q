class Solution:
    """
    input - list
    output - list of reversed string
    edge cases? empty list? 
    """
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s)-1
        while l<=r:
            var = s[l]
            s[l] = s[r]
            s[r] = var
            l+= 1
            r-=1 

        