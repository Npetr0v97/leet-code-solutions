# Given a string s, find the length of the longest substring without duplicate characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        strSet = set()
        finalSet = set()
        original_pointer = 0
        pointer = 0
        while True:
            prev_len_set = len(strSet)

            print()
            print(strSet, finalSet)

            strSet.add(s[pointer])

            if len(strSet) == prev_len_set:
                if len(finalSet) < len(strSet):
                    finalSet = strSet
                    if len(finalSet) > len(s) // 2:
                        break

                if s[pointer] != s[pointer-1]:
                    original_pointer += 1
                    pointer = original_pointer
                strSet = set((s[pointer]))

            print(strSet, finalSet)
            if pointer == len(s) - 1:
                break
            else:
                pointer += 1

        if len(finalSet) < len(strSet):
            finalSet = strSet

        return len(finalSet)


x = Solution()
s = "spftzkihkrpunhxuhejormgjhsdwqswihbdjolsydisqprnyxwmokuxrndpdvmncntl"

print(x.lengthOfLongestSubstring(s))
