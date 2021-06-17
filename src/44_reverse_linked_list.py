# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        prev = None
        while node:
            curr_next = node.next
            node.next = prev

            prev = node
            node = curr_next
        return prev

    def reverseList1(self, head: ListNode) -> ListNode:
        head_new = None
        current_node = head
        previous_node = None
        while current_node:
            next_node = current_node.next
            if not previous_node:  # start of list is new end
                current_node.next = None
                head_new = current_node
            else:  # point backwards
                current_node.next = previous_node
                head_new = current_node
            previous_node = current_node
            current_node = next_node
        return head_new


if __name__ == "__main__":
    nodes_list = [1, 2, 3, 4, 5]
    prev = None
    for val in nodes_list:
        list_node = ListNode(val)
        if prev:
            prev.next = list_node
        else:
            head = list_node
        prev = list_node

    def print_list(head):
        node = head
        while node:
            print(f'ListNode.val={node.val}')
            node = node.next

    print('--- orig list ---')
    print_list(head)

    print('\n--- reversed ----')
    s = Solution()
    new_head = s.reverseList(head)
    print_list(new_head)
