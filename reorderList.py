class Solution:
    def (self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nList = []
        copy = head
        while copy:
            nList.append(copy.val)
            copy = copy.next
        l, r = 0, len(nList) - 1
        copy = head
        while l <= r:
            copy.val = nList[l]
            copy = copy.next
            l += 1
            if copy == None:
                break
            copy.val = nList[r]
            copy = copy.next
            r -= 1
        return head