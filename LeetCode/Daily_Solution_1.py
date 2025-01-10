from collections import Counter

class Daily_Solution_1(object):
    @staticmethod
    def get_char_freq(word):
        return Counter(word)

    @staticmethod
    def get_max_freq(words):
        max_freq = Counter()
        for word in words:
            word_freq = Solution.get_char_freq(word)  
            for char, freq in word_freq.items():  
                max_freq[char] = max(max_freq[char], freq) 
        return max_freq

    @staticmethod
    def is_universal(word, max_freq):
        word_freq = Solution.get_char_freq(word)
        for char, freq in max_freq.items(): 
            if word_freq[char] < freq: 
                return False
        return True

    def wordSubsets(self, words1, words2):
        max_freq = self.get_max_freq(words2)
        return [word for word in words1 if self.is_universal(word, max_freq)]  
