# Last updated: 9/2/2026, 9:20:43 AM
1class Solution:
2
3    def generateMatrix(self, n: int) -> List[List[int]]:
4        
5        counter = 1
6
7        top = left = 0
8
9        bottom = right = n - 1
10
11        lst = [[0]*n for _ in range(n)]
12
13        while top <= bottom and left <= right:
14
15            for pos in range(left,right+1):
16
17                lst[top][pos] = counter 
18
19                counter += 1
20
21            top += 1
22
23            for pos in range(top,bottom+1):
24
25                lst[pos][right] = counter
26
27                counter += 1
28
29            right -= 1
30
31            if top <= bottom :
32
33                for pos in range(right,left-1,-1):
34
35                    lst[bottom][pos] = counter
36
37                    counter += 1
38
39                bottom -= 1
40
41            if left <= right :
42
43                for pos in range(bottom,top-1,-1):
44
45                    lst[pos][left] = counter
46
47                    counter += 1
48
49                left += 1
50
51        return lst