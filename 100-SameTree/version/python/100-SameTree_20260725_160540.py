# Last updated: 7/25/2026, 4:05:40 PM
1class Solution:
2    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
3        # Are both p and q None?
4        if not p and not q:
5            return True
6
7        # Is one of them None?
8        if not p or not q:
9            return False
10
11        # Are their values different?
12        if p.val != q.val:
13            return False
14
15        # Recursive call to the next level down
16        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)