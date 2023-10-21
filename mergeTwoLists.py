class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        head = result
        while list1 and list2:
            if list1.val <= list2.val:
                result.next = list1
                result = result.next
                list1 = list1.next
            else:
                result.next = list2
                result = result.next
                list2 = list2.next
        #残りは繋げるだけで、残りがつながる。
        while list1:
            result.next = list1
            result = result.next
            list1 = list1.next
        while list2:
            result.next = list2
            result = result.next
            list2 = list2.next
        return head.next