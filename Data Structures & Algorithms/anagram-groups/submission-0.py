
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        if len(strs) == 1:
            return [strs]

        groups = defaultdict(list)
    
        for word in strs:
            key = [0]*26
            for letter in word:
                real = ord(letter) - ord('a')
                key[real]+=1
            groups[tuple(key)].append(word)
        return list(groups.values())