'''
The algorithm uses two pointers (fast and slow) to traverse the linked list.
By the time fast reaches the end, slow will be at the middle of the list.
'''

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        prev = ListNode ( 0 )
        prev.next = head
        slow = prev
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # as slow.next is the middle node, we need to set slow.next = slow.next.next
        slow.next = slow.next.next
        return prev.next

