# Last updated: 8/4/2026, 11:09:14 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
8
9        if not head or left == right:
10            return head
11
12        dummy = ListNode(0, head)
13        prev = dummy
14
15        for _ in range(left - 1):
16            prev = prev.next
17
18        cur = prev.next
19        for _ in range(right - left):
20            temp = cur.next
21            cur.next = temp.next
22            temp.next = prev.next
23            prev.next = temp
24
25        return dummy.next