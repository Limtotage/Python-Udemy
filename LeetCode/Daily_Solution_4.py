class Daily_Solution_4(object):
    def findThePrefixCommonArray(self, A, B):
        n= len(A)
        C = [0]*n
        SetA = set()
        SetB = set()
        count=0
        for i in range(n):
            if A[i] not in SetA:
                SetA.add(A[i])
                if A[i] in SetB:
                    count+=1
            if B[i] not in SetB:
                SetB.add(B[i])
                if B[i] in SetA:
                    count+=1
            C[i]=count
        return C

        
