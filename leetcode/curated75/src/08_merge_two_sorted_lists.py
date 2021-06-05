from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'ListNode val={self.val}'


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1

        node_l1 = l1
        node_l2 = l2
        prev = ListNode(-1000)
        head = prev
        while True:
            if node_l1.val <= node_l2.val:
                prev.next = node_l1
                prev = node_l1
                node_l1 = node_l1.next
            elif node_l1.val > node_l2.val:
                prev.next = node_l2
                prev = node_l2
                node_l2 = node_l2.next

            if not node_l1:
                prev.next = node_l2
                break
            if not node_l2:
                prev.next = node_l1
                break

        return head.next

    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_start_node = ListNode()
        current_end = new_start_node
        while l1 and l2:
            if l1.val < l2.val:
                current_end.next = l1
                l1 = l1.next
            else:
                current_end.next = l2
                l2 = l2.next
            current_end = current_end.next

        if l1:
            current_end.next = l1
        elif l2:
            current_end.next = l2

        return new_start_node.next


if __name__ == "__main__":

    def build_list(arr: List) -> ListNode:
        head = ListNode(None)
        prev = None
        for val in arr:
            list_node = ListNode(val)
            if prev:
                prev.next = list_node
            else:
                head = list_node
            prev = list_node
        return head

    def print_list(head):
        node = head
        while node:
            print(f"ListNode.val={node.val}")
            node = node.next
        print()

    nodes_list1 = [1, 2, 4]
    nodes_list2 = [1, 3, 4]

    print("--- orig lists ---")
    l1 = build_list(nodes_list1)
    l2 = build_list(nodes_list2)
    print_list(l1)
    print_list(l2)

    print("--- merged ----")
    s = Solution()
    new_head = s.mergeTwoLists(l1, l2)
    print_list(new_head)
