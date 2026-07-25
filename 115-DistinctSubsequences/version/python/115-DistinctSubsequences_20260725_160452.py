# Last updated: 7/25/2026, 4:04:52 PM
1class Solution:
2    def numDistinct(self, s, t):
3        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
4        for col in range(len(dp[0])):
5            dp[0][col] = 1
6        for x in range(1, len(s) + 1):
7            for y in range(1, len(t) + 1):
8                if s[x - 1] == t[y - 1]:
9                    dp[y][x] = dp[y - 1][x - 1] + dp[y][x - 1]
10                else:
11                    dp[y][x] = dp[y][x - 1]
12        return dp[-1][-1]