class Daily_Solution_3(object):
    def minimumLength(self, s):
        letters = [0]*26
        for c in s:
            letters[ord(c)-ord('a')]+=1
            if letters[ord(c)-ord('a')]%3==0 : 
                letters[ord(c)-ord('a')]/=3
        return sum(letters)
    

        
