class Solution(object):
    def reverseWords(self, s):
       ham=s.strip()
       kelimeler = ham.split()
       output = " ".join(reversed(kelimeler))
       return output
