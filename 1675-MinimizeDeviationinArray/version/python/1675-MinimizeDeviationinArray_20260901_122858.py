# Last updated: 9/1/2026, 12:28:58 PM
1import heapq
2
3class Solution:
4    def minimumDeviation(self, nums: List[int]) -> int:
5        if not nums:
6            return float('inf')
7        
8        evens = []
9        min_val = float('inf')
10        
11        for num in nums:
12            if num % 2 == 0:
13                heapq.heappush(evens, -num)
14                min_val = min(num, min_val)
15            else:
16                heapq.heappush(evens, -num * 2)
17                min_val = min(num * 2, min_val)
18                
19        res = float('inf')
20        while evens[0] % 2 == 0:
21            max_val = -heapq.heappop(evens)
22            res = min(res, max_val - min_val)
23            new_num = max_val // 2
24            heapq.heappush(evens, -new_num)
25            min_val = min(new_num, min_val)
26            
27        res = min(-evens[0] - min_val, res)
28        return res