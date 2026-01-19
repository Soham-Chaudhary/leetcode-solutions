"""
Problem: Sum of Beauty of All Substrings

Beauty of a substring is defined as:
    max(character frequency) - min(character frequency)
(only considering characters that appear in the substring)

This file contains:
1. A naive solution (my initial approach)
2. An optimized solution (recommended)
"""

from collections import Counter, defaultdict


class SolutionNaive:
    """
    Naive Approach (Initial Solution)

    Strategy:
    - Generate all substrings
    - Store them in a list
    - For each substring:
        - Use Counter to calculate character frequencies
        - Compute beauty
        - Add to total sum

    Time Complexity: O(n^3)
    Space Complexity: O(n^3)

    This solution is correct but inefficient and not scalable.
    """

    def beautySum(self, s: str) -> int:
        substrings = []
        total_beauty = 0

        # Generate all substrings
        for i in range(len(s)):
            l = len(s)
            while l > i:
                substrings.append(s[i:l])
                l -= 1

        # Compute beauty for each substring
        for sub in substrings:
            freq = Counter(sub)
            total_beauty += max(freq.values()) - min(freq.values())

        return total_beauty


class SolutionOptimized:
    """
    Optimized Approach (Recommended Solution)

    Strategy:
    - Fix a starting index i
    - Expand the substring character by character
    - Maintain frequency counts incrementally
    - Compute beauty on the fly

    Time Complexity: O(n^2)
    Space Complexity: O(1) (bounded by 26 lowercase letters)

    This solution is efficient and interview-ready.
    """

    def beautySum(self, s: str) -> int:
        n = len(s)
        total_beauty = 0

        for i in range(n):
            freq = defaultdict(int)

            for j in range(i, n):
                freq[s[j]] += 1
                total_beauty += max(freq.values()) - min(freq.values())

        return total_beauty


# Example usage (for local testing)
if __name__ == "__main__":
    s = "aabcb"

    naive = SolutionNaive()
    optimized = SolutionOptimized()

    print("Naive Solution Output:", naive.beautySum(s))
    print("Optimized Solution Output:", optimized.beautySum(s))
