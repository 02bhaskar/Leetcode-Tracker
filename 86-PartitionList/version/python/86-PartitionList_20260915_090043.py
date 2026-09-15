# Last updated: 9/15/2026, 9:00:43 AM
1class Solution:
2    temp = None
3
4    def flatten(self, root):
5        self.helper(root)
6
7    def helper(self, root):
8        if root is None:
9            return
10
11        left = root.left
12        right = root.right
13
14        if self.temp is not None:
15            self.temp.right = root
16
17        root.left = None
18        self.temp = root
19
20        self.helper(left)
21        self.helper(right)