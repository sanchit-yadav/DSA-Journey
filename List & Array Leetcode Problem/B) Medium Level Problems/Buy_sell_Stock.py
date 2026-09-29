# Problem : In an array you are given stocks prices Where You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

from typing import List
def max_profit(nums: List[int]):
    min_price = float('inf')
    max_profit = 0

    for price in nums:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

# Example usage
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    result = max_profit(prices)
    print(result)
        