"""
LeetCode 5 - Longest Palindromic Substring
Link: https://leetcode.com/problems/longest-palindromic-substring/

Approach:
1. Brute Force (commented for reference)
2. Optimal Approach - Expand Around Center

Language: Python
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Optimal Approach: Expand Around Center

        Idea:
        - Every palindrome expands from its center
        - A center can be:
            a) One character (odd length)
            b) Between two characters (even length)
        - Expand around each possible center and track the longest palindrome

        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """

        start, end = 0, 0

        for center in range(len(s)):
            # Odd length palindrome
            len1 = self._expand_from_center(s, center, center)
            # Even length palindrome
            len2 = self._expand_from_center(s, center, center + 1)

            max_len = max(len1, len2)

            # Update start and end indices if a longer palindrome is found
            if max_len > end - start:
                start = center - (max_len - 1) // 2
                end = center + max_len // 2

        return s[start:end + 1]

    def _expand_from_center(self, s: str, left: int, right: int) -> int:
        """
        Expands outward from the given center and returns
        the length of the palindrome.
        """

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        # Length of palindrome
        return right - left - 1


# ------------------------------
# Brute Force (for reference)
# ------------------------------
"""
Approach:
- Generate all substrings
- Check each substring if it is a palindrome
- Return the longest one

Time Complexity: O(n^3)
Space Complexity: O(n^2)

This approach is NOT optimal and is kept only for learning purposes.
"""

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         palindromes = []
#
#         for i in range(len(s)):
#             for j in range(i + 1, len(s) + 1):
#                 substring = s[i:j]
#                 if substring == substring[::-1]:
#                     palindromes.append(substring)
#
#         return max(palindromes, key=len)
