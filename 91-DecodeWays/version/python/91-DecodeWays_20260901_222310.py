# Last updated: 9/1/2026, 10:23:10 PM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        dp = [True] + [False] * len(s)
4
5        for i in range(1, len(s) + 1):
6            for word in wordDict:
7                start = i - len(word)
8                if start >= 0 and dp[start] and s[start:i] == word:
9                    dp[i] = True
10                    break
11
12        return dp[-1]
13        