class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binary = ""
        a_decimalform = 0
        b_decimalform = 0

        for index, element in enumerate(a[::-1]):
            conv_a = int(element)
            if conv_a != 0:
                a_decimalform += conv_a * (2 ** index)
        
        for index, element in enumerate(b[::-1]):
            conv_b = int(element)
            if conv_b != 0:
                b_decimalform += conv_b * (2 ** index)
        
        fdecimalform = a_decimalform + b_decimalform
        
        if fdecimalform == 0:
            return "0"

        while fdecimalform > 0:
            remainder = fdecimalform % 2
            binary += str(remainder)
            fdecimalform = fdecimalform // 2

        return(binary[::-1])