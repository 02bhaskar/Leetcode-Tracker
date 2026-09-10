# Last updated: 9/10/2026, 10:44:58 PM
1class Solution:
2    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
3        self.ans = 0
4        def dfs(node):
5            if not node:
6                return 0, 0
7            left_sum, left_cnt = dfs(node.left)
8            right_sum, right_cnt = dfs(node.right)
9            total_sum = left_sum + right_sum + node.val
10            total_cnt = left_cnt + right_cnt + 1
11            if total_sum // total_cnt == node.val:
12                self.ans += 1
13            return total_sum, total_cnt
14        dfs(root)
15        return self.ans