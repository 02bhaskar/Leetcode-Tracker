// Last updated: 10/1/2026, 2:48:15 PM
1public class Solution {
2    public boolean isValidBST(TreeNode root) {
3        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
4    }
5    
6    public boolean isValidBST(TreeNode root, long minVal, long maxVal) {
7        if (root == null) return true;
8        if (root.val >= maxVal || root.val <= minVal) return false;
9        return isValidBST(root.left, minVal, root.val) && isValidBST(root.right, root.val, maxVal);
10    }
11}