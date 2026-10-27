class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)
        
        while start < end:
            if numbers[start] + numbers[end-1] == target:
                return [start+1, end]
            elif numbers[start] + numbers[end-1] > target:
               end -= 1
            else:
               start += 1
        return [start+1, end]

        

        
        