# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

class Solution:
    def romanToInt(self, s: str) -> int:
        mappingDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        previos_char_value = 0
        sum = 0
        for i, char in enumerate(s):
            current_char_value = mappingDict[char]
            # print(
            #     f"Current: {current_char_value}  /  Previous: {previos_char_value}")

            if current_char_value > previos_char_value and previos_char_value != 0:

                sum = sum + current_char_value - (2 * previos_char_value)
            else:
                sum += current_char_value

            # print("current sum: ", sum)
            previos_char_value = mappingDict[char]

        return sum


x = Solution()

str1 = "III"
str2 = "LVIII"
str3 = "MCMXCIV"
print(x.romanToInt(str1))
print(x.romanToInt(str2))
print(x.romanToInt(str3))
