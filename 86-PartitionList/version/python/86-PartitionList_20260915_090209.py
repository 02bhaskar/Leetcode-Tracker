# Last updated: 9/15/2026, 9:02:09 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        profit = 0
4
5        # Every upward step can be taken as a separate transaction.
6        # Adding all positive day-to-day gains equals the optimal total profit.
7        for i in range(1, len(prices)):
8            if prices[i] > prices[i - 1]:
9                profit += prices[i] - prices[i - 1]
10
11        return profit