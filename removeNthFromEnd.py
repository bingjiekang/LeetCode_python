#----1-----36 ms	14.9 MB
"""删除列表倒数第n个节点可以先通过遍历一遍，得到节点的个数，然后判断出删除的节点位于正数的第几位，然后遍历到对应位数，然后更改指针的指向即可"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        First_head = head  #创建一个指向head的First_head指针用来遍历得到节点的个数
        sult_head = head   #用来得到并更新最终结果
        num = 0   #计数节点的个数
        while First_head!=None:
            num += 1
            First_head = First_head.next
        num = num-n+1   #得到要删除的接点位于正数的第几位
        temp_head = head   #临时指针 用来对目标节点进行删除
        while temp_head!=None:
            num-=1
            if num==1:
                temp_head.next = temp_head.next.next
                break
            elif num==0:         #如果是只有一个节点，直接将头指针指向下一个节点即可
                sult_head = sult_head.next
            temp_head = temp_head.next
        return sult_head
