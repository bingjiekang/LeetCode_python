#----1-----56 ms	15.1 MB
#查询相邻最长子字符串方法：创建一个空列表，依次读入字符，若字符在列表中存在，则删除从最开始到出现这个字符位置的全部数据，读入这个新字符，若这个长度大于当前的最大长度，则sm存储这个长度。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lt = []
        sm = 0
        for i in s:
            if i in lt:
                del lt[0:lt.index(i)+1]#删除从0到出现这个字符内的全部数据
            lt.append(i)
            if(len(lt)>sm):
                sm=len(lt)
        return sm
            
