# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for price in prices:
            if price < buy:
                buy = price
            else:
                diff = price - buy
                if  diff > profit:
                    profit = diff
        return profit

            
            
        
