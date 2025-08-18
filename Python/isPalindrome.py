# Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_num = str(x)
        answer = True
        for i, num in enumerate(string_num):
            index_mirror_item = len(string_num) - i - 1
            # print(string_num[i], string_num[index_mirror_item])
            if string_num[i] != string_num[index_mirror_item]:
                answer = False
                break
            if i == len(string_num) // 2:
                break
        return answer


x = Solution()

num1 = 0

print(x.isPalindrome(num1))
