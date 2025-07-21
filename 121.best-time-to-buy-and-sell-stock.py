#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = prices[0]
        sell_price = prices[0]
        profit = 0

        for index,  price in enumerate(prices):
            if price > sell_price and index != 0:
                sell_price = price
            elif price < buy_price:
                buy_price = price
                sell_price = price

            if buy_price < sell_price:
                profit = max(profit, sell_price - buy_price)
            
            
        return profit
# @lc code=end

solution = Solution()

prices = [7,1,5,3,6,4]

print(solution.maxProfit(prices))