# Last updated: 9/8/2026, 9:07:21 AM
1class Solution(object):
2    def licenseKeyFormatting(self, s, k):
3        s = s.replace('-', '').upper()
4        n = len(s)
5        first_group = n % k or k
6        res = [s[:first_group]]
7        for i in range(first_group, n, k):
8            res.append(s[i:i + k])
9        return '-'.join(res)