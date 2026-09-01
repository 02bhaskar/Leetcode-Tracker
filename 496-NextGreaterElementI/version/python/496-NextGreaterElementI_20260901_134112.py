# Last updated: 9/1/2026, 1:41:12 PM
1class Solution(object):
2    def findLUSlength(self, a, b):
3        if a==b:
4            return -1
5        else:
6            return max(len(a),len(b))
7        