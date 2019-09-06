class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged = ListNode(0)
        node = merged
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1, node = l1.next, node.next
            else:
                node.next = l2
                l2, node = l2.next, node.next
        node.next = l1 if l1 else l2 if l2 else None
        return merged.next
