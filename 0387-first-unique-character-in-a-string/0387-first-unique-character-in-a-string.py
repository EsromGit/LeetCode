class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for index, element in enumerate(s):
            if element in dict:
                dict[element] = (dict[element][0] + 1, dict[element][1])
            else:
                dict[element] = (1, index)

        for key,values in dict.items():
            if values[0] == 1:
                return values[1]
        return -1
