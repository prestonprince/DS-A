# Given a string s, return the longest palindromic substring in s

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        max_len = 0

        for i in range(len(s)):
            l = r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    res = s[l:r+1]
                    max_len = r - l + 1
                l -= 1
                r += 1
            
            l = i
            r = i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    res = s[l:r+1]
                    max_len = r - l + 1
                l -= 1
                r += 1
        return res
