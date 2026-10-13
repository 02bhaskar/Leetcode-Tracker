# Last updated: 10/13/2026, 10:53:03 PM
1class Solution:
2    def maxAlternatingSum(self, nums: List[int]) -> int:
3        a = sorted(x * x for x in nums)
4        k = len(nums) // 2  
5        return sum(a[k:]) - sum(a[:k])