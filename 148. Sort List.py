# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def Middle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s, f = head, head
        while f and f.next and f.next.next:
            f = f.next.next
            s = s.next
        return s
    
    def Merge(self, left_side: Optional[ListNode],right_side: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while left_side and right_side:
            if left_side.val > right_side.val:
                tail.next = right_side
                right_side = right_side.next
            else:
                tail.next = left_side
                left_side = left_side.next
            tail = tail.next
        tail.next = left_side if left_side else right_side
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        mid = self.Middle(head)
        right = mid.next
        mid.next = None

        left_side = self.sortList(head)
        right_side = self.sortList(right)

        return self.Merge(left_side,right_side)
      
