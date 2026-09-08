# Last updated: 9/8/2026, 9:09:19 AM
1class Solution:
2    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
3        ans = 0
4        for i in range(1, len(timeSeries)):
5            ans += min(duration, timeSeries[i] - timeSeries[i-1])
6
7        return ans + duration
8
9        