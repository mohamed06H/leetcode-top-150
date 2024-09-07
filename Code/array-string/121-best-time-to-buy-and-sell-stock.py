class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Initialize max profit
        max_profit = 0

        # Find max profit 
        for i in range(len(prices)-1):
            buy_price = prices[i]
            sell_prices = prices[i+1:]
            # Get max sell price - buy price 
            profit = max(sell_prices) - buy_price
            # Compare with previous max profit
            if profit > max_profit:
                max_profit = profit

        return max_profit
