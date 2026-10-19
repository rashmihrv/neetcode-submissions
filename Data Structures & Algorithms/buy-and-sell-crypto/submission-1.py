class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) > 1:
            minNum = prices[0]
            profit = float("-inf")

            for i in range(1, len(prices)):
                if prices[i] < minNum:
                    minNum = prices[i]

                profit = max(profit, prices[i] - minNum)
            return profit
        else:
            return 0