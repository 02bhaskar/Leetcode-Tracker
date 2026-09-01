# Last updated: 9/1/2026, 10:19:01 PM
1class Solution(object):
2    def isInterleave(self, s1, s2, s3):
3
4        if len(s3) != len(s1) + len(s2) :
5            return False 
6
7        last  = set()  # ((i,j) , (i2,j2))  
8        last.add((-1,-1))
9
10        for i in range(len(s3)):   # cal f(i) 
11            tmp = set()
12            for (m,n) in last :   #(i,j)
13                if m+1 <len(s1) and s3[i] == s1[m+1]:
14                    tmp.add((m+1,n))
15                if n+1 <len(s2) and s3[i] == s2[n+1]:
16                    tmp.add((m,n+1))
17            last = tmp
18            if not last:
19                return False
20
21        return True