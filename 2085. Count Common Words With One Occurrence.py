from collections import Counter

class Solution(object):
    def countWords(self, words1, words2):
        count1 = Counter(words1)
        count2 = Counter(words2)
        
        ans = 0
        for w in count1:
            if count1[w] == 1 and count2[w] == 1:
                ans += 1
                
        return ans