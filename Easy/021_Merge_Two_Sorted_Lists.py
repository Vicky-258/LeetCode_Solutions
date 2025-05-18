from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        list3 = ListNode()

        temp1, temp2, temp3 = list1, list2, list3

        while temp1 and temp2:

            if temp1.val <= temp2.val:

                temp3.next = temp1

                temp1, temp3 = temp1.next, temp3.next

            else:

                temp3.next = temp2

                temp2, temp3 = temp2.next, temp3.next

        if temp1:

            temp3.next = temp1

        else:

            temp3.next = temp2

        return list3.next
