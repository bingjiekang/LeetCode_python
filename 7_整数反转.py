#----1-----36 ms	15 MB
class Solution:
    def reverse(self, x: int) -> int:
        m=0
        if x>0:
            while x>0:
                m= m*10 + x%10
                x//=10
        else:
            x = (-1)*x
            while x>0:
                m= m*10 + x%10
                x//=10
            m = (-1)*m
        t = 2**31

        if m<(-1)*t or m>(t-1):
            m = 0
        return m
            
