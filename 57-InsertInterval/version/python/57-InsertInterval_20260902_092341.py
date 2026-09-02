# Last updated: 9/2/2026, 9:23:41 AM
1class Solution:
2    def setZeroes(self, matrix: List[List[int]]) -> None:
3
4        m = len(matrix)
5        n = len(matrix[0])
6		
7        first_row_has_zero = False
8        first_col_has_zero = False
9        
10        for row in range(m):
11            for col in range(n):
12                if matrix[row][col] == 0:
13                    if row == 0:
14                        first_row_has_zero = True
15                    if col == 0:
16                        first_col_has_zero = True
17                    matrix[row][0] = matrix[0][col] = 0
18    
19        for row in range(1, m):
20            for col in range(1, n):
21                matrix[row][col] = 0 if matrix[0][col] == 0 or matrix[row][0] == 0 else matrix[row][col]
22        
23        if first_row_has_zero:
24            for col in range(n):
25                matrix[0][col] = 0
26        
27        if first_col_has_zero:
28            for row in range(m):
29                matrix[row][0] = 0
30        