class Daily_Solution_13:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count =0
        i=-1 
        j = -1
        for k in range(len(s1)):
            if s1[k] != s2[k]:
                count+=1
                if i== -1: i=k
                elif j==-1: j=k
        if count == 0 : return True
        elif count == 2 and s1[j] == s2[i] and  s1[i]== s2[j]:
            return True
        return False
""" alternative zip function
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        zipped=[(x,y) for x,y in zip(s1,s2) if x!=y]
        return len(zipped)==0 or (len(zipped)==2 and zipped[0][0]==zipped[1][1] and zipped[0][1]==zipped[1][0])"""
        
        
