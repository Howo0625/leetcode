class Solution(object):
    def addTwoNumbers(self, l1, l2):
        nodel = ListNode(0)
        ans = nodel
        temp = 0

        while l1 or l2 or temp:
            cur1 = l1.val if l1 else 0
            cur2 = l2.val if l2 else 0

            total = cur1 + cur2 + temp
            temp = total // 10
            ans.next = ListNode(total % 10)
            ans = ans.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return nodel.next
