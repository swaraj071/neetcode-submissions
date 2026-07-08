# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        total = 0
        tmp = dummy.next
        while tmp:
            tmp = tmp.next
            total += 1
        
        if n == total:
            return head.next
        
        to_remove = total - n + 1
        node_id = 1
        tmp = dummy.next
        prev = None
        while tmp and node_id < to_remove:
            prev = tmp
            tmp = tmp.next
            node_id += 1
        
        prev.next = tmp.next
        return dummy.next


