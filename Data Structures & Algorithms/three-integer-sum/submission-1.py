class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_list = sorted(nums)
        print(sorted_list)
        result = []

        left, right = 0, len(nums)-1
        third_pointer = 0

        while left < right:
            temp_sum = sorted_list[left] + sorted_list[right] + sorted_list[right-1]
            if temp_sum == 0:
                if [sorted_list[left], sorted_list[right], sorted_list[right-1]] not in result:
                    print("kommt rein: " , temp_sum)
                    result.append([sorted_list[left], sorted_list[right], sorted_list[right-1]])
                    
                
            elif temp_sum > 0:
                right -= 1
            else:
                left += 1
        print(result)
        return result
                
