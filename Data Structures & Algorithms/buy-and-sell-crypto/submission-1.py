class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 0
        n = len(prices)
        profit = 0
        
        for i in range(1, n):
            if prices[i] < prices[buy]:
                buy = i
            elif prices[i] > prices[sell]: 
                sell = i
            
            if buy>sell: sell = buy
            profit = max(profit, prices[sell]-prices[buy])
        return profit
            