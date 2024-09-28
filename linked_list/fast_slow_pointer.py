'''
   Source: Leetcode - Prob 876: Middle of the Linked List
   Description: Given the head of a singly linked list, return the middle node of the linked list
                If there are two middle nodes, return the second middle node             
   Output: Middle node of the linked list
   Technique: Fast and slow pointer to traverse linked list
   Student: Jackie Chan
   Known bugs: None
   Date: 09/27/2024
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_ptr = head
        fast_ptr = head
        while fast_ptr and fast_ptr.next: 
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr

# Example usage:
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Find the middle node
    solution = Solution()
    middle_node = solution.middleNode(head)
    print("Middle node value:", middle_node.val)  # Output should be 3