class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] is not hashmap:
                hashmap.setdefault(nums[i], [])

            hashmap[nums[i]].append(nums[i])
        
        print(k)
        print(len(hashmap))
        return sorted(list(hashmap)[len(hashmap)-k:len(hashmap)])
        