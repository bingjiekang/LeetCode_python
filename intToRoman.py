#----1-----56 ms	14.7 MB
"""数字转换成罗马数字，将罗马数中某些特定数字罗列模拟出来，再使用时字典查找即可。
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        Dict = {0:"",1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",
10:"X",20:"XX",30:"XXX",40:"XL",50:"L",60:"LX",70:"LXX",80:"LXXX",90:"XC",
100:"C",200:"CC",300:"CCC",400:"CD",500:"D",600:"DC",700:"DCC",800:"DCCC",900:"CM",
1000:"M",2000:"MM",3000:"MMM"}   #模拟出罗马数字对应的数字
        lt = []   #用来存放数字每位的大小
        temp = 1  #用来辅助分离出数字的大小
        sult = []  #存放最后转换的罗马数字
        while(num>0): 
            sm = num%10
            sm*=temp  
            lt.append(sm)  #加入对应的数字
            temp*=10
            num//=10
        for i in lt[::-1]:   #倒序读取数字 
            sult.append(Dict[i])  #转换成对应的罗马数字
        sult = "".join(sult)
        return sult




