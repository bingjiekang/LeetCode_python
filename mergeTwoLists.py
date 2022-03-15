#----1-----40 ms	14.9 MB
"""合并两个有序链表，通过比较每个节点对应的数据大小，将小的节点数据加入到新的链表中，当一个链表中的节点全部读取完后，剩下的链表可以直接放到新的链表后方"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None:   #首先判断若两个链表都为空 则直接返回
            return list1
        elif list1==None and list2!=None:   #一个链表为空 另一个不为空，直接返回另一个链表
            return list2
        elif list1!=None and list2==None:
            return list1
        sult_list = ListNode()     #新链表 用来得到两列表合并后的新链表
        Sult_List = sult_list      #指向新链表头的指针 用来返回最后答案
        temp_tranfer = sult_list   #用来得到当一个链表中止后 另一个链表剩余节点的数据
        while list1!=None and list2!=None:    #开始对两个链表进行合并
            sult_list.next = ListNode(None)  #对新链表后一个节点进行申请内存空间
            if list1.val<=list2.val:   #用来比较两链表中数据较小的节点
                temp = list1.val        #存储最小节点的数据
                sult_list.val = temp    #对新链表节点数据进行赋值
                list1 = list1.next      #对应链表节点向后移动
            else:
                temp = list2.val         #和if条件判断里的一样
                sult_list.val = temp
                list2 = list2.next
            temp_tranfer = sult_list     #当一个链表中节点读取完 另一个链表节点数据未读取完，用来存放未读取完的链表的对应地址
            sult_list = sult_list.next   #对新链表节点进行更新
        sult_list = temp_tranfer         #把对应未读取完的链表地址赋值给新链表
        if list1==None and list2==None:   #通过判断 对新链表接上未读取完的链表的余下的节点的值
            return Sult_List
        elif list1==None and list2!=None:
            sult_list.next = list2
        elif list1!=None and list2==None:
            sult_list.next = list1
        return Sult_List    



