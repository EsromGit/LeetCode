class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = []
        start = 0
        end = len(s) - 1
        vowels = ['a','e', 'i', 'o', 'u','A','E', 'I', 'O', 'U']

        for char in s:
            lst.append(char)

        while start < end:
            if lst[start] in vowels and lst[end] in vowels:
                lst[start], lst[end] = lst[end],lst[start]
                start += 1
                end -= 1
            elif lst[start] in vowels and lst[end] not in vowels:
                end -= 1
            elif lst[end] in vowels and lst[start] not in vowels:
                start += 1
            else:
                start += 1
                end -= 1
        ans = ''.join(lst)
        return ans