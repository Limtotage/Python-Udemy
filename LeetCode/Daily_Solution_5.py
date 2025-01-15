class Daily_Solution_5(object):
    def addbit (self,num,count):
        temp =0
        while count>0:
            while (((num>>temp)&1)==1):
                temp+=1
            num |= (1<<temp)
            count-=1
        return num
    def removebit (self,num,count):
        while count>0:
            num&=(num-1)
            count-=1
        return num
    def minimizeXor(self, num1, num2):
        c1=bin(num1).count('1')
        c2=bin(num2).count('1')
        if c1>c2 :
            return self.removebit(num1,c1-c2)
        elif c2>c1:
            return self.addbit(num1,c2-c1)
        return num1
        
