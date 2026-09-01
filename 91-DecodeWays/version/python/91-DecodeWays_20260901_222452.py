# Last updated: 9/1/2026, 10:24:52 PM
1class Solution:
2    def compareVersion(self, v1: str, v2: str) -> int:
3        v1, v2 = list(map(int, v1.split('.'))), list(map(int, v2.split('.')))  
4        for rev1, rev2 in zip_longest(v1, v2, fillvalue=0):
5            if rev1 == rev2:
6                continue
7
8            return -1 if rev1 < rev2 else 1 
9
10        return 0