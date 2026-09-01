# Last updated: 9/1/2026, 10:13:43 PM
1class Solution(object):
2    def diameterOfBinaryTree(self, root):
3        def diameter(node, res):
4            if not node:
5                return 0
6            
7            left = diameter(node.left, res)
8            right = diameter(node.right, res)
9
10            res[0] = max(res[0], left + right)
11            
12            return max(left, right) + 1
13        
14        res = [0]
15        diameter(root, res)
16        return res[0]