"""
LeetCode - Trionic Array I
Link: https://leetcode.com/problems/trionic-array-i/?envType=daily-question&envId=2026-02-04

Approach:
- Find the end of the first strictly increasing segment (peak p).
- Find the end of the strictly decreasing segment (valley q).
- Find the end of the second strictly increasing segment.
- Valid if all three segments are non-empty and the traversal ends at the last index.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 1

        while i < n and nums[i - 1] < nums[i]:
            i += 1
        p = i - 1

        while i < n and nums[i - 1] > nums[i]:
            i += 1
        q = i - 1

        while i < n and nums[i - 1] < nums[i]:
            i += 1
        r = i - 1

        return (p != 0) and (q != p) and (r == n - 1 and r != q)
