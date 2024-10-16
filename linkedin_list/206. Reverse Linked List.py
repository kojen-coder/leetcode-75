class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = None
        curr = head

        while curr != None:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node
        return prev
