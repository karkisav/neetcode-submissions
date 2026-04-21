# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy, curr = head, head
        prev = None
        l = 0
        while curr:
            l += 1
            curr = curr.next
        
        curr = head

        if (not curr or not curr.next) and l == n:
            return 

        i = 0
        while i <= l - n - 1:
            prev = curr
            curr = curr.next
            i += 1

        print("remove:", curr.val)

        if prev:
            print("prev", prev.val)

        if prev:
            prev.next = curr.next
            curr.next = None
            
        if not prev:
            dummy = dummy.next

        return dummy