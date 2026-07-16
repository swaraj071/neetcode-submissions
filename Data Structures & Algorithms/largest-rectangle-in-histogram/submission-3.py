class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stack=[]
        max_area=0
        for i in range(n):
            while stack and heights[i]<heights[stack[-1]]:
                height=heights[stack.pop()]
                nse=i
                pse=stack[-1] if stack else -1
                max_area=max(max_area,height*(nse-pse-1))
                print(height*(nse-pse-1))
            stack.append(i)
        while stack:
            nse=n
            height=heights[stack.pop()]
            pse=stack[-1] if stack else -1
            max_area=max(max_area,height*(nse-pse-1))
        

        return max_area
        