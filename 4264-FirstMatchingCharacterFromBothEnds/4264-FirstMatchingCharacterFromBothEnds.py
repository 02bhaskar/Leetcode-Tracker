# Last updated: 7/9/2026, 3:05:14 PM
class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n=len(s)
        for i in range(n):
            if s[i]==s[n-i-1]:
                return i
        return -1
        