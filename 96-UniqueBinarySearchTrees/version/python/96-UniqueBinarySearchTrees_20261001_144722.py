# Last updated: 10/1/2026, 2:47:22 PM
1class Solution:
2    def numTrees(self, n: int) -> int:
3        uniq_tree = [1] * (n + 1)
4        
5        for nodes in range(2, n + 1):
6            total = 0
7            for root in range(1, nodes + 1):
8                total += uniq_tree[root - 1] * uniq_tree[nodes - root]
9            uniq_tree[nodes] = total
10        
11        return uniq_tree[n]