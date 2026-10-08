# Last updated: 10/8/2026, 10:18:47 AM
1class Solution:
2    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
3        window = set()
4        for i in range(len(nums)):
5            if nums[i] in window:
6                return True
7            
8            window.add(nums[i])
9            
10            if len(window) > k:
11                window.remove(nums[i-k])
12        
13        return False