class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 0
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < prices[buy]:
                buy = i
            elif prices[i] > prices[sell]: 
                sell = i
            
            if buy>sell: sell = buy
            profit = max(profit, prices[sell]-prices[buy])
        return profit
            