class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split(" ")
        str = []
        for element in lst:
            if element == '':
                continue
            str.append(element)
        ans = ' '.join(str[::-1])
        return ans