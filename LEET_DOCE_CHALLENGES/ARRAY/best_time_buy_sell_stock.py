"""
You are given an pricesay "prices" where prices[i] is the price of
a given stock on the i'th day. You want to maximize your profit by
choosing a single day to but one stock and choosing a different day
in the future to sell that stock. Return the maximum profit you can
achieve from this transaction. If you cannot achieve any profit
return 0.
"""


class BuySellStock:
    @staticmethod
    def result(prices: list[int]) -> int:
        min_value = prices[0]
        max_profit = 0

        for i in range(0, len(prices)):
            if prices[i] < min_value:
                min_value = prices[i]
            else:
                potential_price = prices[i] - min_value
                if potential_price > max_profit:
                    max_profit = potential_price
        return max_profit


prices = [2, 5, 4, 3, 5, 7, 1, 5]
buy_sell_stock = BuySellStock.result(prices)
print(buy_sell_stock)


'''
class BuySellStock:
    @staticmethod
    def result(prices: list[int]) -> int:
        min_value = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_value:
                min_value = price
            else:
                potential_profit = price - min_value
                if potential_profit > max_profit:
                    max_profit = potential_profit

        return max_profit
'''
