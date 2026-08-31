# Last updated: 8/31/2026, 10:24:09 PM
1class Solution(object):
2    def isPalindrome(self, s: str) -> bool:
3        new = ""
4        for i in s:
5            if i.isalnum():
6                new += i.lower()
7        return new == new[::-1]