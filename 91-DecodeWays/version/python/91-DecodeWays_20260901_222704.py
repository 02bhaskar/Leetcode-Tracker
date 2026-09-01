# Last updated: 9/1/2026, 10:27:04 PM
1from functools import cmp_to_key
2
3class Solution:
4    def largestNumber(self, nums: List[int]) -> str:
5        num_strs = list(map(str, nums))
6        
7        def compare(x, y):
8            if x + y > y + x:
9                return -1 
10            elif x + y < y + x:
11                return 1 
12            else:
13                return 0   
14        
15        num_strs.sort(key=cmp_to_key(compare))
16        
17        largest_num = ''.join(num_strs)
18        
19        return '0' if largest_num[0] == '0' else largest_num