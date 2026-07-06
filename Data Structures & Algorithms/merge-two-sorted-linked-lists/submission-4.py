# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # list1=[1,2,4]
        # list2=[1,3,5]

        # list1=[3,4,7]
        # list2=[1,3,5]
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            dummy = node = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next
                node = node.next
            
            if not list1:
                node.next = list2
            else:
                node.next = list1
        return dummy.next









