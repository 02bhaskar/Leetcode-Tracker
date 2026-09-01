# Last updated: 9/1/2026, 10:17:51 PM
1class Solution(object):
2    def restoreIpAddresses(self, s):
3        """
4        :type s: str
5        :rtype: List[str]
6        """
7        def backtrack(start, current):
8            if len(current) == 4:
9                if start == len(s):
10                    result.append('.'.join(current))
11                return
12
13            for length in range(1, 4):
14                if start + length <= len(s):
15                    segment = s[start:start+length]
16                    if self.is_valid(segment):
17                        current.append(segment)
18                        backtrack(start + length, current)
19                        current.pop()
20
21        result = []
22        backtrack(0, [])
23        return result
24
25    def is_valid(self, segment):
26        if len(segment) > 3 or (len(segment) > 1 and segment[0] == '0'):
27            return False
28        value = int(segment)
29        return 0 <= value <= 255