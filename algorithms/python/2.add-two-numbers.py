'''
给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

num1_node1 = ListNode(2)
num1_node2 = ListNode(4)
num1_node3 = ListNode(3)
num1_node1.next = num1_node2
num1_node2.next = num1_node3

num2_node1 = ListNode(5)
num2_node2 = ListNode(6)
num2_node3 = ListNode(4)
num2_node1.next = num2_node2
num2_node2.next = num2_node3

l1 = num1_node1
l2 = num2_node1

class Solution1:
    def addTwoNumbers(self, l1, l2):
        res = ListNode(0)
        head = res
        carry = 0
        while l1 or l2 or carry!=0:
            sum = carry
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next
            if sum<=9:
                res.val = sum
                carry = 0
            else:
                res.val = sum%10
                carry = sum//10
            if l1 or l2 or carry!=0:
                res.next = ListNode(0)
                res = res.next
        return head

#简洁版
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = p = ListNode(None)
        carry = 0
        while l1 or l2 or carry:
            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(carry%10)
            p = p.next
            carry //=10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next