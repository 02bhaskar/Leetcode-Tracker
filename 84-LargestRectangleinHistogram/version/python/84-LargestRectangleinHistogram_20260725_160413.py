# Last updated: 7/25/2026, 4:04:13 PM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        stack = [-1]
4        max_area = 0
5
6        for i in range(len(heights)):
7            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
8                height = heights[stack.pop()]
9                width = i - stack[-1] - 1
10                max_area = max(max_area, height * width)
11            stack.append(i)
12        
13        while stack[-1] != -1:
14            height = heights[stack.pop()]
15            width = len(heights) - stack[-1] - 1
16            max_area = max(max_area, height * width)
17        
18        return max_area