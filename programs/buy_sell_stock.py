# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

#Example 1:
# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if not n:
            return 0
        profit, buy, sell = 0, "", ""
        curr_action = "buy"
        for i in range(0, n-1):
            if curr_action == "sell":
                sell = prices[i]
                if sell > prices[i+1] and sell > buy:
                    print("selling.......", sell, buy)
                    profit += sell - buy
                    curr_action = "buy"
                    sell, buy = 0, 0

            elif curr_action == "buy" and prices[i] < prices[i+1]:
                print("buying....", prices[i])
                buy = prices[i]
                curr_action = "sell"
                sell = 0

        if curr_action == "sell" and buy != "" and prices[n-1] > buy:
            profit += prices[n-1] - buy

        return profit

s = Solution()
res = s.maxProfit([2,1,2,0,1])
print("res **********************", res)

