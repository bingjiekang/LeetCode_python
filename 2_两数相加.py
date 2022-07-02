#----1-----60 ms	15 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        l4 = l3
        while(l1!=None or l2!=None):
            if (l1 == None):
                l1 = ListNode()
                l1.next = None
            elif (l2 == None):
                l2 = ListNode()
                l2.next = None
            l3.val = l3.val+l1.val+l2.val
            if(l1.next==None and l2.next==None):
                l3.next=None
            else:
                l3.next=ListNode()
            if(l3.val>9):
                l3.val %=10
                if(l3.next==None):
                    l3.next=ListNode(1)
                else:
                    l3.next.val+=1
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next
        return l4

#----2-----60 ms	14.8 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum1=0
        l3 = ListNode()
        l4 = l3
        i = 0
        j=0
        while(l1!=None):
            sum1+=l1.val*10**i
            l1 = l1.next
            i+=1
        while(l2!=None):
            sum1+=l2.val*10**j
            l2 = l2.next
            j+=1
        while(sum1>0):
            l3.val = sum1%10
            sum1//=10
            if(sum1!=0):
                l3.next=ListNode()
                l3 = l3.next
        return l4
