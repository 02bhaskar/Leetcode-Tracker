# Last updated: 9/2/2026, 9:21:58 AM
1class Solution:
2    def minPathSum(self, grid: List[List[int]]) -> int:
3        m=len(grid)
4        n=len(grid[0])
5        prev=[0]*n
6        for i in range(m):
7            cur=[0]*n
8            for j in range(n):
9                if i==0 and j==0:
10                    cur[j]=grid[i][j]
11                else:
12                    up=grid[i][j]
13                    if i>0:
14                        up+=prev[j]
15                    else:
16                        up+=float('inf')
17                    left=grid[i][j]
18                    if j>0:
19                        left+=cur[j-1]
20                    else:
21                        left+=float('inf')
22                    cur[j]=min(up,left)
23            prev=cur
24        return prev[n-1]
25
26        