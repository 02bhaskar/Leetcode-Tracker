# Last updated: 9/2/2026, 9:31:50 AM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        res = []
4        subset = []
5
6        def create_subset(i):
7            if i == len(nums):
8                res.append(subset[:])
9                return
10            
11            subset.append(nums[i])
12            create_subset(i+1)
13
14            subset.pop()
15            create_subset(i+1)
16
17        create_subset(0)
18        return res