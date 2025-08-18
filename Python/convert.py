# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        counter = 0
        final_string = ""
        array_string = list(s)
        num_rows = numRows
        if num_rows == 1:
            return s
        # init list with empty lists (matrix)
        matrix = [[] for i in range(num_rows)]
        while True:
            subtract = False
            for i, char in enumerate(array_string):
                matrix[counter].append(char)

                if counter == num_rows-1:
                    subtract = True
                elif counter == 0:
                    subtract = False

                if subtract:
                    counter -= 1
                else:
                    counter += 1
            break

        for row in matrix:
            # print(row)
            final_string += "".join(row)
        return final_string


x = Solution()

str1 = "ABCsdsasdadsa"
num_rows = 4

print(x.convert(str1, num_rows))
