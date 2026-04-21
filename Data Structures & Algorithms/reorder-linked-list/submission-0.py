# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def find_mid(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow


        def reverse_list(head):

            prev, curr = None, head

            while curr:

                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev
        
        def merge(head1, head2):

            while head2:
                tmp1, tmp2 = head1.next, head2.next
                head1.next = head2
                head2.next = tmp1
                head1, head2 = tmp1, tmp2

        mid = find_mid(head)
        head_rev = reverse_list(mid.next)
        mid.next = None
        merge(head, head_rev)
