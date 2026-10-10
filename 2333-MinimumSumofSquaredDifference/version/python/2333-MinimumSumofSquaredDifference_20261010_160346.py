# Last updated: 10/10/2026, 4:03:46 PM
1
2class Solution:
3    def minSumSquareDiff(self, nums1, nums2, k1, k2):
4        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
5        k = k1 + k2
6
7        max_diff = max(diff)
8
9        freq = [0] * (max_diff + 1)
10        for d in diff:
11            freq[d] += 1
12
13        for d in range(max_diff, 0, -1):
14            if k == 0:
15                break
16
17            count = freq[d]
18            if count == 0:
19                continue
20
21            use = min(k, count)
22            freq[d] -= use
23            freq[d - 1] += use
24            k -= use
25
26        if k > 0:
27            return 0
28
29        return sum(d * d * freq[d] for d in range(len(freq)))
30