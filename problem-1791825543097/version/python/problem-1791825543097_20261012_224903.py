# Last updated: 10/12/2026, 10:49:03 PM
1class Solution:
2    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
3        freq={}
4        ans = []
5        for x in nums1:
6            freq[x]=freq.get(x,0)+1
7        for x in nums2:
8            if x in freq and freq[x]>0:
9                ans.append(x)
10                freq[x]-=1
11        
12
13        return ans