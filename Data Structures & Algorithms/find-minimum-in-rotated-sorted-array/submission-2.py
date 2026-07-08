class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while nums[start] > nums[end]:
            pivot = (start + end) // 2
            if nums[pivot] < nums[pivot - 1]:
                return nums[pivot]
            if nums[pivot] >= nums[start]:
                start = pivot + 1
            else:
                end = pivot - 1
        
        return nums[start]