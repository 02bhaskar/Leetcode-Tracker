# Last updated: 9/1/2026, 1:46:30 PM
1class Solution:
2    def __init__(self):
3        self.prev = float('inf')
4        self.ans = float('inf')
5    
6    def getMinimumDifference(self, root):
7        self.inOrder(root)
8        return self.ans
9    
10    def inOrder(self, root):
11        if root.left:
12            self.inOrder(root.left)
13        
14        self.ans = min(self.ans, abs(root.val - self.prev))
15        self.prev = root.val
16        
17        if root.right:
18            self.inOrder(root.right)
19        