class Solution:
    """
    understand:
    - input - two strings
    -output - boolean
    edgecases:
    - will the strings contain letters only? will it be lower, upper or both?
    - what if the strings are empty?
    match:
        - strings - pointers
        - iteration
        - dictionary
    planning:

    """
    def isAnagram(self, s: str, t: str) -> bool:
        s_new = "".join(sorted(s))
        t_new = "".join(sorted(t))
        return s_new == t_new
        