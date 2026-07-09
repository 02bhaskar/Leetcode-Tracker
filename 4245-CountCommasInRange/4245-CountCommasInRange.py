# Last updated: 7/9/2026, 3:05:16 PM
class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        else:
            return n - 999