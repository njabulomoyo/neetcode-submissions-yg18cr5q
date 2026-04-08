class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}

        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str not in str_dict:
                str_dict[sorted_str] = []
            str_dict[sorted_str].append(str)

        return str_dict.values()
            
        



        
        