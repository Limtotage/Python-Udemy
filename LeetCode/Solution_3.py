class Solution_3(object):
    def compress(self, chars):
        index=0
        yazlan=""
        while index<len(chars):
            harf=chars[index]
            say =0
            while index<len(chars) and chars[index]==harf:
                index+=1
                say+=1
            if say > 1 :
                yazlan += harf+str(say)
            else:
                yazlan+=harf
        i=0
        for x in yazlan:
            chars[i]=x
            i+=1
        return len(yazlan)
        
