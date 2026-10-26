class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            print(i)
            for j in range(len(numbers)):
                
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
    
        return []