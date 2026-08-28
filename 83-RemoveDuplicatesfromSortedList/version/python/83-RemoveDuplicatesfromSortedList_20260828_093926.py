# Last updated: 8/28/2026, 9:39:26 AM
1class Solution:
2    def deleteDuplicates(self, head):
3        current = head
4
5        while current and current.next:
6            if current.val == current.next.val:
7                current.next = current.next.next
8            else:
9                current = current.next
10
11        return head