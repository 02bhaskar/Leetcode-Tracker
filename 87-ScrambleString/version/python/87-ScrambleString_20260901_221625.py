# Last updated: 9/1/2026, 10:16:25 PM
1class Solution(object):
2    def isScramble(self, s1, s2):
3        """
4        :type s1: str
5        :type s2: str
6        :rtype: bool
7        """
8
9        n = len(s1)
10
11        if len(s2) != n:
12            return False
13
14        if s1 == s2:
15            return True
16
17
18        if n == 1:
19            return False
20
21        key = s1 + " " + s2
22
23        if key in self.mp:
24            return self.mp[key]
25
26        for i in range(1, n):
27            without_swap = (
28                self.isScramble(s1[:i], s2[:i])
29                and
30                self.isScramble(s1[i:], s2[i:])
31            )
32
33            if without_swap:
34                return True
35
36            with_swap = (
37                self.isScramble(s1[:i], s2[n-i:])
38                and
39                self.isScramble(s1[i:], s2[:n-i])
40            )
41
42            if with_swap:
43                return True
44
45        self.mp[key] = False
46        return False
47
48    mp = {}