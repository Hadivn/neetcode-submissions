class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        print(range(len(numbers)))
        for i in range(1, len(numbers)):
            print(i)
            if numbers[i] + numbers[i+1]:
                res.append(i)
                res.append(i+1)
                return res
        
        return res
        