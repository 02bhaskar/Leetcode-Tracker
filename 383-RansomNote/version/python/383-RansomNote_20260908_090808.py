# Last updated: 9/8/2026, 9:08:08 AM
1class Solution:
2    def findMaxConsecutiveOnes(self, a: List[int]) -> int:
3        return max(accumulate(a,lambda q,v:q*v+v))