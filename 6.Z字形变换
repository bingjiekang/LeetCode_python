#----1-----	60 ms	15 MB
#通过规律总结变换后的每一行对应的字符串的下标，对应输入到列表中，最后转换成字符串即可
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        length = len(s)
        fist_endl = (numRows-1)*2   #首行、末行间距
        cj = numRows-2              #除首、未行其他行之间的差的个数
        lt = []
        for i in range(numRows):    #i 为转换后的每行开始时第一个元素所对应的下标同时也是第几行的标识
            temp = i                #temp为转换后的每行要加入的原字符串的下标
            while(temp<length):     
                lt.append(s[temp])  #中间主列 即所转换成的z图中，每列有numrows个元素的列
                if i==0 or i==(numRows-1): #首行、未行
                    temp+=fist_endl    #首行或末行 间距为(numRows-1)*2 （转换行数-1）*2
                else:               #其他行
                    temp+=(cj*2)    #除首、未行其他行之间 “z中部”的实际下标   “z中部” 指对于除首、未行外，其他行对应的除中间主列外的其他的列，每列只有一个元素
                    if temp<length:  
                        lt.append(s[temp])  
                        temp+=((numRows-1)-cj)*2   #将temp更新到 最新主列
            if i!=0 and i!=(numRows-1):  #控制除首、未行其他行之间的差的个数
                cj-=1
        s = "".join(lt)             #列表转换成字符串
        return s
            
            


        
