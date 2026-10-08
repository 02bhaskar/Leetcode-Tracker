# Last updated: 10/8/2026, 9:32:08 AM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        nums.sort()
4
5        for i in range(1, len(nums)):
6            if nums[i] == nums[i - 1]:
7                return True
8        
9        return False