class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        words = title.split()
        res = []
        
        for word in words:
            if len(word) <= 2:
                res.append(word.lower())
            else:
                res.append(word.capitalize())        
        return " ".join(res)