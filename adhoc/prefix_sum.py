'''
   Source: Leetcode - Prob 1480: Running Sum of 1d Array
   Description: Given an array, nums, find a running sum of that array as 
                runningSum[i] = sum(nums[0]...nums[i])            
   Output: Running sum array
   Techniques Used: Prefix sum
   Author: Jackie Chan
   Known Bugs: None
   Date: 09/27/2024
'''
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            result.append(sum)
        return result
    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4]  # Example input
    running_sum = solution.runningSum(nums)
    print("Running Sum:", running_sum)  # Output should be [1, 3, 6, 10]
