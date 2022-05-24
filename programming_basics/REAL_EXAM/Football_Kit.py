price_shirt = float(input())
price_to_meet = float(input())

price_per_shirt = price_shirt

short_price = price_per_shirt * 0.75
socks_price = short_price * 0.20
shoes_price = (price_shirt + short_price) * 2
sum_without_discount = price_shirt + short_price + socks_price + shoes_price
sum_with_discount = sum_without_discount * 0.85
diff = abs(sum_with_discount - price_to_meet)

if sum_with_discount >= price_to_meet:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {sum_with_discount:.2f} lv.")
else:
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")