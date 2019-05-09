#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = curr = 0
        for i in nums:
            prev, curr = curr, max(prev + i, curr)
        return curr

