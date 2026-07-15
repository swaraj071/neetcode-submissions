class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_p=1
        r_p=1
        n=len(nums)
        output=[1]*n
        for i in range(n):
            output[i]=l_p
            l_p=l_p*nums[i]
        for i in range(n-1,-1,-1):
            output[i]=output[i]*r_p
            r_p=r_p*nums[i]
        return output        

# T: O(n+n) =O(n)
# S: O(n)


