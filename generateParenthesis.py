#----1-----32 ms	15.1 MB
"""有效括号排序：通过递归实现深度搜索DFS，例如两个括号，括号有效的只有()(),(()),即左括号一定比相应的右括号先出现，即在出现的括号序列中，剩余需要出现的右括号次数一定比左括号次数多，如果剩余的右括号
次数比左括号次数多，则返回上一层，先将左括号加入字符串中，放入递归函数中，当左括号放完后，再放入右括号，满足一定条件将结果加入列表中，不满足则回退，以此实现递归调用"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lt = []    #用来存放有序的括号序列
        Some_Sult = ""    #暂时存放括号的排序序列
        def Similar_Dfs(Char_Str,left,right):  #定义递归函数，通过反复递归调用实现深度搜索获得对应结果
            if left==0 and right==0:   #递归出口即深度搜索底部，当对应的左括号和右括号满足条件要求全部输入到序列中时，加入到列表中。
                lt.append(Char_Str)    #将满足的序列加入到列表中
                return 0
            if left>right:   #当对应的右括号出现在对应的左括号前面时，返回上一层。
                return 0
            if left>0:   #向序列中放入左括号，递归调用，不满足调用函数里的对应的某些条件时，返回到上一层
                Similar_Dfs(Char_Str+"(",left-1,right)
            if right>0:  #向序列中放入右括号，递归调用，不满足调用函数里的对应的某些条件时，返回到上一层
                Similar_Dfs(Char_Str+")",left,right-1)
        Similar_Dfs(Some_Sult,n,n)  #调用开始
        return lt
