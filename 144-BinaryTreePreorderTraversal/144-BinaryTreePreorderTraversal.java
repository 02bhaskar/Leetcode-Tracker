// Last updated: 7/9/2026, 3:08:08 PM
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        helper(root, ans);
        return ans;
    }
    public static void helper(TreeNode root, List<Integer> ans){
        if (root == null){
            return;
        }
        ans.add(root.val);
        helper(root.left, ans);
        helper(root.right, ans);
    }
}