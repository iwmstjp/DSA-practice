lass Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        copy = head
        dummyHead = ListNode()
        dummyHead.next = head
        count = 1
        while copy and copy.next:
            copy = copy.next
            count += 1
        position = count - n + 1
        count = 0
        copy = dummyHead
        previousNode = copy
        copy = copy.next
        while copy:
            count += 1
            # print(f"count: {count}, p:{previousNode}, c:{copy}")
            if count == position:
                previousNode.next = copy.next
                break
            previousNode = previousNode.next
            copy = copy.next
        return dummyHead.next