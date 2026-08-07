# Last updated: 8/7/2026, 10:07:24 PM
1class Solution:
2    def predictTheWinner(self, nums: List[int]) -> bool:
3        n = len(nums)
4        if n % 2 == 0: 
5            return True
6            
7        dp = list(nums)
8        for i in range(n - 2, -1, -1):
9            for j in range(i + 1, n):
10                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
11        return dp[-1] >= 0