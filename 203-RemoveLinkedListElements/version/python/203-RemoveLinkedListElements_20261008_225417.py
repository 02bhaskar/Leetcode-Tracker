# Last updated: 10/8/2026, 10:54:17 PM
1class Solution:
2    def removeElements(self, head, val):
3        """
4        :type head: ListNode
5        :type val: int
6        :rtype: ListNode
7        """
8        
9        dummy_head = ListNode(-1)
10        dummy_head.next = head
11        
12        current_node = dummy_head
13        while current_node.next != None:
14            if current_node.next.val == val:
15                current_node.next = current_node.next.next
16            else:
17                current_node = current_node.next
18                
19        return dummy_head.next