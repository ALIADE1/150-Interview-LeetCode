# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        if head.next and head.val == head.next.val:
            curr = head
            while curr and curr.val == head.val:
                curr = curr.next
            return self.deleteDuplicates(curr)

        else:
            head.next = self.deleteDuplicates(head.next)
            return head
          
