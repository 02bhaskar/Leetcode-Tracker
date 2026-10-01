# Last updated: 10/1/2026, 2:48:56 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def recoverTree(self, root: TreeNode | None) -> None:
9        k=float("-inf")
10        self.first=self.sec=self.prev=None
11        current =root
12        while current:
13            if current.left is None:
14                if current.val<k:
15                    if not self.first:
16                        self.first=self.prev
17                    self.second=current
18                k=current.val
19                self.prev=current
20                current=current.right
21            else:
22                pred=current.left
23                while pred.right and pred.right!=current:
24                    pred=pred.right
25                if pred.right is None:
26                    pred.right=current
27                    current=current.left
28                else:
29                    pred.right=None
30                    
31                    if current.val<k:
32                        if not self.first:
33                            self.first=self.prev
34                        self.second=current
35                    k=current.val
36                    self.prev=current
37                    current=current.right
38            
39        self.first.val,self.second.val=self.second.val,self.first.val
40
41
42            
43            
44
45
46            
47       
48        