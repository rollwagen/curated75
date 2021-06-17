import sys

prices = [7, 1, 5, 3, 6, 4]  # 5
prices = [7, 6, 4, 3, 1]  # 0
prices = []

max_profit, buy = 0, sys.maxsize

for _, sell in enumerate(prices):
    if sell < buy:
        buy = sell
    else:
        profit = sell - buy
        max_profit = max(max_profit, profit)

print(max_profit)
