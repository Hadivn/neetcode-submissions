class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for i in range(len(strs)):
            hashmap.setdefault("".join(sorted(strs[i])), []).append(strs[i])

        result = list(hashmap.values())      
        return result