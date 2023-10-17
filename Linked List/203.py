# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        while head != None and head.val == val:
            head = head.next

        current = head
        while current != None and current.next != None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return head
        
