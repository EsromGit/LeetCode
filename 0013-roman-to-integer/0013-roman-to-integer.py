class Solution:
    def romanToInt(self, s: str) -> int:
        map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0

        for i in range(len(s)):
            current_value = map[s[i]]

            if i < len(s) -1:
                next_value = map[s[i+1]]

                if current_value < next_value:
                    sum -= current_value
                else:
                    sum += current_value
            else:
                sum += current_value
        return sum