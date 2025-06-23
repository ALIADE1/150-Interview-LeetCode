# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head.next
        dummy = ListNode()
        tail = dummy
        current_sum = 0
        
        while current:
            if current.val == 0:
                tail.next = ListNode(current_sum)
                tail = tail.next
                current_sum = 0
            else:
                current_sum += current.val
            current = current.next
        
        return dummy.next
