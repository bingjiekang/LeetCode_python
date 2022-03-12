#----1-----36 ms	14.9 MB
"""通过队列进行排列组合，先模拟出全部数字对应的英文，然后通过依次读取数字，然后通过队列弹出第一个数和加入的新的数，加入到原来队列中，最后得到的队列就是结果"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        Dict = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],  #模拟出全部对应数据
        "6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        sult = []      #用来存储结果
        length_index = len(digits)   #得到字符串的长度，用来得到举例范围
        if length_index==0:   #如果为空 直接返回空列表
            return sult
        else:
            for i in range(length_index):  #最外层循环 获得每个字符的对应数字，用来查询对应字典里的数据
                length = len(sult)      #获得并更新此时结果的长度
                if length == 0:    #如果等于0 则证明还没有放入数据
                    for j in Dict[digits[i]]:   #对sult进行更新存储最新数据
                        sult.append(j)
                else:
                    for l in range(length_dx):   #sult存在原有数据 对原数据的长度依次举例 便于弹出原来的每个数据 最外层循环
                        temp = sult.pop(0) 
                        for r in Dict[digits[i]]:   #内层循环 对此时字符对应字典里的数据进行依次读取，并和sult弹出的数据进行整合并放入
                            sult.append(temp+r)
                length_dx = len(sult)    #用来存储当前sult的长度 便于下次进行外层循环时 进行遍历
            return sult 
            
