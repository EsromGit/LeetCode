# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head

        prev, curr = dummy, head

        while curr and curr.next:
            # Save pointers and next pair
            nextPair = curr.next.next
            second = curr.next

            # Swap pair
            second.next = curr
            prev.next = second
            curr.next = nextPair

            # Update next pair
            prev = curr
            curr = nextPair

        return dummy.next
        