#----1-----40 ms	14.9 MB
"""依次交换两个节点，不使用其他空间，直接交换节点，例如1,2,3,4,5,6,7交换后应该是2,1,4,3,6,5,7。即2后面是1，1后面是4，4后面是3，3后面是6，6后面是5，由于7后面没有数则7后面是5。
First_head保存待交换节点的左边那个节点，Second_head保存带交换节点的右边那个节点，
若Second_head后面有2个剩余的节点以上，则将First_head连接到Second_head.next.next，Second_head连接到First_head,将Second_head指向Second_head.next.next(first_head),
过中间变量将First_head指向Second_head.next；
若Second_head后面只有两个节点，则在本次循环中将节点改变即可
若Second_head后面只有一个节点，则将First_head连接到Second_head.next，Second_head连接到First_head即可结束
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:   #如果链表中只有一个节点或者没有节点直接返回即可
            return head
        First_head = head    #待交换节点的左节点
        Second_head = head.next  #待交换节点的右节点
        sult_head = Second_head   #用来返回正确答案的节点
        while Second_head.next!=None:   #如果Second_head后面还有节点，可以继续循环
            if Second_head.next.next == None:   #如果Second_head.next后面没有节点则将左节点连接到右节点后一个节点，右节点连接到左节点，返回即可
                First_head.next = Second_head.next
                Second_head.next = First_head
                return sult_head
            First_head.next = Second_head.next.next     #Second_head后面至少有两个节点，将左节点连接到Second_head.next.next即右节点后面的后面
            temp = ListNode()   #临时节点，用来存储第二个待交货的两个节点中的左节点
            temp = Second_head.next   
            Second_head.next = First_head   #将右节点接左节点后面
            Second_head = First_head.next   #更新节点到下一个对应待交换的节点位置
            First_head = temp    #更新节点到下一个对应待交换的节点位置
            if Second_head.next==None:  #如果此时Second_head后面已无节点，则将右节点连接上左节点，左节点连接上右节点后面的None即可
                First_head.next = Second_head.next
                Second_head.next =First_head
                return sult_head
        First_head.next = Second_head.next  #链表中只有两个节点交换这两个节点即可
        Second_head.next = First_head
        return sult_head
