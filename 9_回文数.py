#----1-----72 ms	14.9 MB
#通过将数字倒着依次取出，并放入新的变量中 若相同则返回True 否则返回False，如果数小于0 则返回False
class Solution:
    def isPalindrome(self, x: int) -> bool:
        m = x
        sult = 0
        if x<0:
            return False
        while m>0:
            sult=sult*10+m%10
            m//=10
        if sult==x:
            return True
        else:
            return False
            
            
#----2-----60 ms	14.9 MB
#若数据小于0则返回False，否则转化成字符型数据，通过判断对应着的数据是否相同，若全部相同则返回True，否则返回False
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        y = str(x)
        length = len(y)
        for i in range(length//2):
            if y[i]==y[length-1-i]:#判断前后对应着的数据是否相等
                pass
            else:
                return False
        return True
        
        
