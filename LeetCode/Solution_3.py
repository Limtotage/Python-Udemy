class Solution_3(object):
    def compress(self, chars):
        index=0
        yazlan=0
        while index<len(chars):
            harf=chars[index]
            say =0
            while index<len(chars) and chars[index]==harf:
                index+=1
                say+=1
            chars[yazlan]=harf
            yazlan+=1
            if say > 1 :
                for c in str(say):
                    chars[yazlan] = c
                    yazlan += 1
        return yazlan
