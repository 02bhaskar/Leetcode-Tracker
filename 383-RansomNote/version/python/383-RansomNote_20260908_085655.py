# Last updated: 9/8/2026, 8:56:55 AM
1from typing import List
2
3class Solution:
4    def firstUniqChar(self, s: str) -> int:
5        counts = [0] * 26
6        for c in s:
7            counts[ord(c) - ord('a')] += 1
8        for i, c in enumerate(s):
9            if counts[ord(c) - ord('a')] == 1:
10                return i
11        return -1