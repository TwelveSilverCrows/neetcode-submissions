class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sorting is long
        #use a dictionary for each 'word', then you only do 1 pass
        #return true if both dicts are the same
        #if s and t aren't the same length, they can't be anagrams of each other
        if len(s) != len(t):
            return False

        
        s_dict = {}
        t_dict = {}


        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)

        
        return s_dict == t_dict

        