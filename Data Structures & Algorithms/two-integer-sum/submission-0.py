from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map to store: { value: index }
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # If the complement exists in the map, we found our pair
            if complement in seen:
                # Return indices with the smaller index first
                return [seen[complement], i]
            
            # Otherwise, store the current number and its index in the map
            seen[num] = i