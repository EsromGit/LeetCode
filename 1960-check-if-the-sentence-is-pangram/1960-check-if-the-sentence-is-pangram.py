class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False

        s = set()

        for char in sentence:
            s.add(char)
        
        return len(s) == 26
