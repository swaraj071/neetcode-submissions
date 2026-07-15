class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        mx=0
        for i,h in enumerate(heights):
            strt=i
            while stack and h<stack[-1][1]:
                idx,hg=stack.pop()
                mx=max(mx,hg*(i-idx))
                strt=idx
            stack.append((strt,h))
        for i,h in stack:
            mx=max(mx,h*(len(heights)-i))
        return mx
        