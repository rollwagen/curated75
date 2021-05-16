class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0

        for i in range(len(s)):
            if longest_substring > (len(s) - 1):
                break
            substring = s[i : i + 1]
            length_substring = 1
            for j in range(i + 1, len(s)):
                c = s[j : j + 1]
                if c not in substring:
                    substring += c
                    length_substring += 1
                else:
                    break
                j += 1
            longest_substring = max(length_substring, longest_substring)
            i += 1
        return longest_substring
