class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []

        for i in range(len(numbers)):
            if numbers[i] + numbers[i+1] == target:
                res.append(i+1)
                res.append(i+2)
                return res
            
            if numbers[i] + numbers[i+1] > target:
                continue
            
        return res
        