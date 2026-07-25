# Last updated: 7/25/2026, 4:02:27 PM
1class Solution:
2    def totalNQueens(self, n: int) -> int:
3        columns = set()
4        main_diag = set()
5        second_diag = set()
6
7        result = 0
8
9        def backtracking(row: int):
10            if row == n:
11                nonlocal result
12                result += 1
13
14            for idx in range(n):
15                md_idx, sd_idx = row - idx, row + idx
16
17                if idx in columns or md_idx in main_diag or sd_idx in second_diag:
18                    continue
19
20                columns.add(idx)
21                main_diag.add(md_idx)
22                second_diag.add(sd_idx)
23
24                backtracking(row + 1)
25
26                second_diag.remove(sd_idx)
27                main_diag.remove(md_idx)
28                columns.remove(idx)
29
30        backtracking(0)
31        return result