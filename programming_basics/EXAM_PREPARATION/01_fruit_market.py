strawberry_price = float(input())
bananas_qty = float(input())
oranges_qty = float(input())
raspberry_qty = float(input())
strawberry_qty = float(input())

raspberry_price = strawberry_price / 2
orange_price = raspberry_price * 0.60
banana_price = raspberry_price * 0.20

total_price = (banana_price * bananas_qty) + \
              (orange_price * oranges_qty) + \
              (raspberry_price * raspberry_qty) + \
              (strawberry_price * strawberry_qty)
print(f"{total_price:.2f}")
