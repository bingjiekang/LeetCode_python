#----1----时间超限
"""类似暴力：依次查找字符，若列表中不存在该字符则放入列表中，若所查找字符已经在列表中，计算出现的所有相同字符到该字符之间是否满足回文子串的形式，若满足则记录最长的长度，将这区间内数据放入另一个
空列表中，依次查找子字符"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lt = []#空列表用来存放字符串s
        length = 0  #用来记录最长回文子字符串的长度
        answer = []  #用来存放最长回文子字符的数据
        for i in s:  #遍历字符串
            if i in lt:  #若字符已经在列表中出现过 则开始计算他们间是否是最长的回文子串
                lt.append(i) #把该字符加如到列表中
                temp_length = len(lt) #temp_length 存放此时lt的长度
                ut = lt.index(i)   #查找第一个出现该字符的下标
                for r in range(ut,temp_length-1):  #查找所有和该字符一样的下标
                    if lt[r]==i:
                        temp = [t for t in lt[r:temp_length]] #如果找到相同字符 则截取他们间的数据内容并放入temp临时列表中
                        lis = [j for j in temp]  #lis同步temp里的数据 若直接用=赋值，则为浅复制，原数据改变，lis内的数据也会改变
                        temp.reverse()   #将temp数组翻转
                        lisd = len(lis)  #得到这个列表中数据的长度
                        if lis == temp and lisd>length: #如果反转后的数据和原数据相同且该列表的长度比原记录最长回文子字符串的长度大 则记录下来
                            length = lisd  #更新最长回文子字符串的长度
                            answer = lis   #更新列表中的数据内容          
            else:
                lt.append(i)  #若字符不存在列表中 直接加入空列表中
        if len(answer)==0:  #如果字符串s只有一个字符或列表中无回文子字符串 则记录第一个数据
            answer = lt[0] 
        answer = "".join(answer)  #列表转字符串
        return answer
        
#----2-----5416 ms	22.9 MB
"""动态规划：若字符串有回文子字符串，则该子字符串最两边的两字符一定相同且内部也满足回文子字符的性质。利用动态规划，将字符串对应一个二维列表[i][j]，行、列的数据都对应着字符串s的数据内容,
dp[i][j]表示下标为i的字符到下标为j的字符是否是回文子字符串，dp[i][j]为1代表下标为i的字符到下标为j的字符是回文子字符串，dp[i][j]为0代表下标为i的字符到下标为j的字符不是回文子字符串，
i到j中间的内容是否是回文子字符串由 下标为i+1到下标为j-1 是否是回文子字符串决定，即dp[i][j]是否为1由dp[i+1][j-1]是否为1决定。首先对二维列表全体赋初值为0，由于单个字符都是回文子字符，
则对角线[0][0],[1][1],[2][2],[3][3]等都是“回文子字符串”，则dp[0][0],dp[1][1],dp[2][2],dp[3][3]赋值为1，然后依次对二维列表中的其他数据根据字符串的是否满足的条件依次对二维列表进行赋值。
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)   #获取字符串s的长度
        max_len = 0       #用来记录最长回文子字符串的长度
        begin_index = 0   #获得最长回文子字符串开始的下标
        dp = [[0]*length for i in range(length)]  #初始化列表 开一个行，列都为字符串s长度的二维列表
        for i in range(length):   #对角线数据都是回文子字符 进行初始化赋值为1 
            dp[i][i] = 1
        for cr in range(1,length): #依次递增下标为i到下标为j字符之间的距离 用来确定下标为i到下标为j字符间是否为回文子字符串
            f = 0         #用来记录开始的下标i 即f相当于dp[i][j]中的i
            while((f+cr)<length):#f+cr 相当于dp[i][j]中的j，确定边界 j小于字符串的最大下标
                if(s[f]==s[f+cr] and (dp[f+1][f+cr-1]==1 or cr==1)):  #如果下标为f(相当于i)和下标为f+cr(相当于j)的字符相同，且下标i+1到j-1间是回文子字符串(或两个字符相邻）则dp[f][f+cr]即dp[i][j]为1
                    dp[f][f+cr] = 1
                    if cr>max_len:    #如果下标为i到下标为j字符之间为回文子字符串且大于最长回文子字符串的长度，则记录下来
                        max_len = cr  #更新最长回文子字符串的长度
                        begin_index = f  #更新最长回文子字符串开始的下标
                f+=1
        return s[begin_index:begin_index+max_len+1]  #截取最长回文子字符串的数据并返回
