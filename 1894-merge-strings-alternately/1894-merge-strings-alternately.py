class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str = ""
        point1 = 0
        point2 = 0
        while point1 < len(word1) and point2 < len(word2):
            str += word1[point1]
            str += word2[point2]
            point1 += 1
            point2 += 1
        
        if len(word2) > len(word1):
            str += word2[point2:]
        else:
            str += word1[point1:]
        return str

