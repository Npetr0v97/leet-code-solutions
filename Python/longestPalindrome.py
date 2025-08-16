# Given a string s, return the longest palindromic substring in s.
# A string is palindromic if it reads the same forward and backward.


"""
Solution: Iterate through all the chars. Firstly, check if we have adjacent duplicate chars. E.g abbba we have triple "b"s. The first while loop
collects those adjacent duplicates and adjusts the pointer. From then on using the pre and post indexes to check letters from both sides of the
original char. Finally we check what was collected as a palindromic substring and we assign it to biggest
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        biggest = ""
        current = ""
        for i, char in enumerate(s):
            current = s[i]

            pre_index = 1
            post_index = 1
            initial_check = False
            secondary_check = False
            while not initial_check:

                if i + post_index < len(s) and s[i+post_index] == s[i]:
                    current += s[i+post_index]
                    post_index += 1
                else:
                    initial_check = True
                    break

            while not secondary_check:
                if i-pre_index >= 0 and i+post_index < len(s) and s[i-pre_index] == s[i+post_index]:

                    current = s[i-pre_index] + current + s[i+post_index]
                    pre_index += 1
                    post_index += 1
                else:
                    secondary_check = True

            if len(current) > len(biggest):
                biggest = current

            current = ""

        return biggest


x = Solution()


str1 = "ccc"
str2 = "abcba"
str3 = "cbbd"
print(x.longestPalindrome(str1))
print(x.longestPalindrome(str2))
print(x.longestPalindrome(str3))
