#----1-----	384 ms	18.8 MB
"""列表中有n个待合并的链表，可以两个两个合并，将合并后的再加入到列表最后，反复直到列表中只剩下一个合并好的链表就是对应的答案，引用了mergeTwo.py"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         def mergeTwo(self, list1: Optional[ListNode], list2: Optional[ListNode]):
#             if list1==None and list2==None:   #首先判断若两个链表都为空 则直接返回
#                 return list1
#             elif list1==None and list2!=None:   #一个链表为空 另一个不为空，直接返回另一个链表
#                 return list2
#             elif list1!=None and list2==None:
#                 return list1
#             sult_list = ListNode()     #新链表 用来得到两列表合并后的新链表
#             Sult_List = sult_list      #指向新链表头的指针 用来返回最后答案
#             temp_tranfer = sult_list   #用来得到当一个链表中止后 另一个链表剩余节点的数据
#             while list1!=None and list2!=None:    #开始对两个链表进行合并
#                 sult_list.next = ListNode(None)  #对新链表后一个节点进行申请内存空间
#                 if list1.val<=list2.val:   #用来比较两链表中数据较小的节点
#                     temp = list1.val        #存储最小节点的数据
#                     sult_list.val = temp    #对新链表节点数据进行赋值
#                     list1 = list1.next      #对应链表节点向后移动
#                 else:
#                     temp = list2.val         #和if条件判断里的一样
#                     sult_list.val = temp
#                     list2 = list2.next
#                 temp_tranfer = sult_list     #当一个链表中节点读取完 另一个链表节点数据未读取完，用来存放未读取完的链表的对应地址
#                 sult_list = sult_list.next   #对新链表节点进行更新
#             sult_list = temp_tranfer         #把对应未读取完的链表地址赋值给新链表
#             if list1==None and list2==None:   #通过判断 对新链表接上未读取完的链表的余下的节点的值
#                 return Sult_List
#             elif list1==None and list2!=None:
#                 sult_list.next = list2
#             elif list1!=None and list2==None:
#                 sult_list.next = list1
#             return Sult_List
        length = len(lists)   #获取列表中的长度
        if length==0:  #若无待合并的链表直接返回None
            return None
        while(length!=1):  #若列表中待排序的链表不止一个，则返回合并直至剩余一个
            if length>=2:
                lists.append(mergeTwo(self,lists[0],lists[1]))  #将两个链表合并到一个链表中，并加入到列表最后
                lists.pop(0) #将前两个弹出列表
                lists.pop(0)  
            length = len(lists)
        return lists[0]   #列表中剩余一个链表，就是该答案
