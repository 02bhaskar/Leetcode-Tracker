# Last updated: 9/8/2026, 8:55:26 AM
1# The guess API is already defined for you.
2# def guess(num: int) -> int:
3
4class Solution:
5    def guessNumber(self, n: int) -> int:
6        beg, end = 1, n
7        while beg <= end:
8            mid = beg + (end - beg) // 2
9            if guess(mid) == 0:
10                return mid
11            elif guess(mid) == 1:
12                beg = mid + 1
13            else:
14                end = mid - 1
15        return 0  # fallback, though problem guarantees a solution