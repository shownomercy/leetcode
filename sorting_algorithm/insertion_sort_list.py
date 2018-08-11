# Algorithm of Insertion Sort:

# Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.

# Difficulty: Medium

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        begin = head

        cursor = head
        cursor_previous = None
        current = head
        previous = None
        while current is not None:
            next = current.next
            cursor = begin
            cursor_previous = None
            while cursor != current:
                if cursor.val > current.val:
                    if cursor_previous is None:
                        # get current_previous and next
                        # move current out by connecting current_previous and current_next
                        # assign current to head (or begin)?
                        # assign current_next to cursor
                        # set current to next, previous does not change
                        previous.next = next
                        begin = current
                        current.next = cursor
                    else:
                        # get current_previous and next
                        # move current out by connect current_previous and current_next
                        # assign current to between cursor_previous and cursor
                        previous.next = next
                        cursor_previous.next = current
                        current.next = cursor
                    break
                # value to update:
                # cursor move on, cursor_previous,
                cursor_previous = cursor
                cursor = cursor.next
            if cursor == current:
                previous = current
            current = next
        return begin


node1 = ListNode(4)
node2 = ListNode(3)
node3 = ListNode(2)
node4 = ListNode(1)
node5 = ListNode(2.5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node6 = Solution().insertionSortList(node1)

while node6:
    print(node6.val)
    node6 = node6.next