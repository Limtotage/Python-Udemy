class Daily_Solution_23:
    def __init__(self):
        self.ans=""
        self.chars=['a', 'b', 'c']
    def backtrack(self,n:int,now:str,length:int,wanted_word):
        if len(now)==n:
            wanted_word[0]-=1
            if wanted_word[0]==0:
                self.ans=now
            return
        for c in self.chars:
            if length == 0 or now[-1]!=c:
                self.backtrack(n,now+c,length+1,wanted_word)
                if wanted_word[0]==0: return 
        
    def getHappyString(self, n: int, k: int) -> str:
        self.ans=""
        self.backtrack(n,"",0,[k])
        return self.ans
        
