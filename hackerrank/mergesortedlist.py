# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_start_node = ListNode()
        current_end = new_start_node
        while l1 and l2:
            if l1.val < l2.val:
                current_end = l1
                l1 = l1.next
            else:
                current_end = l2
                l2 = l2.next
        if l1:
            current_end.next = l1
        elif l2:
            current_end.next = l2

        return new_start_node


if __name__ == "__main__":

    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    # Output: [1,1,2,3,4,4]
    s = Solution()
    s.mergeTwoLists(l1, l2)
