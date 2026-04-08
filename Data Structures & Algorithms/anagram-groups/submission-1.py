class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        """
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str not in str_dict:
                str_dict[sorted_str] = []
            str_dict[sorted_str].append(str)

        return str_dict.values()
        """
        
        for str in strs:
            count = [0]*26
            for letter in str:
                count[ord(letter)-ord("a")] += 1
            ana = tuple(count)
            if ana not in str_dict:
                str_dict[ana] = []
            str_dict[ana].append(str)

        return str_dict.values()

        
            
        



        
        