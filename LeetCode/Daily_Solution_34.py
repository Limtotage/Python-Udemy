class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        #return [i for i, w in enumerate(words) if w.find(x)!=-1]
        res=[]
        idx=0
        for word in words:
            if x in word:
                res.append(idx)
            idx+=1
        return res
