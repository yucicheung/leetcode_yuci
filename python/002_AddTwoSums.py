# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        higher = 0
        outLinkListNode = ListNode(0)
        head = outLinkListNode
        while l1 and l2:
            single_sum = l1.val + l2.val + higher
            outLinkListNode.val = single_sum % 10
            higher = single_sum / 10
            l1 = l1.next
            l2 = l2.next
            if l1 and l2:
                outLinkListNode.next = ListNode(0)
                outLinkListNode = outLinkListNode.next
        while l1:
            outLinkListNode.next = ListNode(0)
            outLinkListNode = outLinkListNode.next
            single_sum = l1.val + higher
            outLinkListNode.val = single_sum % 10
            higher = single_sum / 10
            l1 = l1.next
        while l2:
            outLinkListNode.next = ListNode(0)
            outLinkListNode = outLinkListNode.next
            single_sum = l2.val + higher
            outLinkListNode.val = single_sum % 10
            higher = single_sum / 10
            l2 = l2.next
        if higher>0:
            outLinkListNode.next = ListNode(higher)
            outLinkListNode = outLinkListNode.next
        return head
