# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
import math


class Solution:
    def addTwoNumbers(self, l1, l2):
        current_node_l1 = l1
        l1_sum = 0
        current_node_l2 = l2
        l2_sum = 0
        math_pow = 0
        while current_node_l1:
            new_num = current_node_l1.val
            for power in range(math_pow):
                new_num = new_num * 10

            l1_sum += new_num

            current_node_l1 = current_node_l1.next
            math_pow += 1

        math_pow = 0
        while current_node_l2:
            new_num = current_node_l2.val
            for power in range(math_pow):
                new_num = new_num * 10

            l2_sum += new_num
            current_node_l2 = current_node_l2.next
            math_pow += 1

        final_sum = l1_sum + l2_sum

        current_head = None
        if final_sum == 0:
            return ListNode(final_sum)
        final_head = None
        while True:

            if final_sum == 0:
                return final_head

            derived_number = final_sum % 10

            if current_head is None:
                current_head = ListNode(derived_number)
                final_head = current_head
            else:
                current_head.next = ListNode(derived_number)
                current_head = current_head.next

            final_sum = final_sum // 10


# Solution.addTwoNumbers()
class ListNode:
    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


# Helper to build a linked list from a Python list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head


# l1 = build_linked_list([2, 4, 3])
# l2 = build_linked_list([5, 6, 4])
l1 = build_linked_list([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
l2 = build_linked_list([5, 6, 4])
x = Solution()
print(x.addTwoNumbers(l1, l2))
