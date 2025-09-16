# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        l, r = 0, len(arr) - 1
        while r > l:
            if arr[r] != arr[l]:
                return False
            l+=1
            r-=1

        return True
