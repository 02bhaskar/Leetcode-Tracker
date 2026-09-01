# Last updated: 9/1/2026, 11:59:40 AM
1class Solution:
2    def area(self, heights: List[int]) -> int:
3        stack = []
4        maxArea = 0
5        n = len(heights)
6
7        for i in range(n + 1):
8            h = 0 if i == n else heights[i]
9            while stack and h < heights[stack[-1]]:
10                height = heights[stack.pop()]
11                width = i if not stack else i - stack[-1] - 1
12                maxArea = max(maxArea, height * width)
13            stack.append(i)
14
15        return maxArea
16
17    def maximalRectangle(self, matrix: List[List[str]]) -> int:
18        if not matrix:
19            return 0
20
21        m, n = len(matrix), len(matrix[0])
22        hist = [0] * n
23        ans = 0
24
25        for i in range(m):
26            for j in range(n):
27                if matrix[i][j] == '1':
28                    hist[j] += 1
29                else:
30                    hist[j] = 0
31            ans = max(ans, self.area(hist))
32
33        return ans