# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ans = ListNode()
        h1, h2 = l1, l2
        v1, v2, carry = 0, 0, 0

        while l1 or l2:

            if l1:  
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            
            total = v1 + v2 + carry 
            ans.next = ListNode(total % 10)
            ans = ans.next
            carry = total // 10
            v1, v2 = 0, 0

        if carry == 1:
            ans.next = ListNode(1)

        return dummy.next 