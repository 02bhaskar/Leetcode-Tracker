# Last updated: 8/31/2026, 10:22:31 PM
1class Solution:
2    def generate(self, numRows: int) -> list[list[int]]:
3        pascal = []
4
5        for i in range(numRows):
6            row = [1] * (i + 1) 
7            for j in range(1, i):
8                row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
9            pascal.append(row)
10
11        return pascal