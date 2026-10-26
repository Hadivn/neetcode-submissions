class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] is not hashmap:
                hashmap.setdefault(nums[i], [])

            hashmap[nums[i]].append(nums[i])
        
        sortedList = []
        for key in sorted(hashmap, key=lambda key: len(hashmap[key]), reverse=True):
            sortedList.append(key)
        
        print(sortedList[:k])
        return sortedList[:k]