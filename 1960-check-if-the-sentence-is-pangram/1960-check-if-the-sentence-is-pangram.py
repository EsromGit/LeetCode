class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set()

        for char in sentence:
            s.add(char)
        if len(s) == 26:
            return True
        return False 
