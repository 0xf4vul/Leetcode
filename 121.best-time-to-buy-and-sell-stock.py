#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices):
            low = prices[0]
            for i in range(len(prices)-1):
                if prices[i+1] > prices[i]:
                    profit = max(profit, prices[i+1] - low)
                else:
                    low = min(low, prices[i+1])
        return profit


