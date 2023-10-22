class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        resNode = ListNode()
        head = resNode
        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = total // 10
            resNode.next = ListNode(total % 10)
            l1 = l1.next
            l2 = l2.next
            resNode = resNode.next
        # print(carry)
        while l1:
            total = l1.val + carry
            carry = total // 10
            # print(carry)
            resNode.next = ListNode(total % 10)
            l1 = l1.next
            resNode = resNode.next
        while l2:
            total = l2.val + carry
            carry = total // 10
            resNode.next = ListNode(total % 10)
            l2 = l2.next
            resNode = resNode.next
        if carry == 1:
            resNode.next = ListNode(1)
        return head.next