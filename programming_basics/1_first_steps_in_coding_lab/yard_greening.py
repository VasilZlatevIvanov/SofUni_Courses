one_sq_m = 7.61

how_much_sq_m = float(input())

price_without_discount = how_much_sq_m * one_sq_m
discount_price = price_without_discount * 0.18

end_price = price_without_discount - discount_price

print(f"The final price is: {end_price} lv.")
print(f"The discount is: {discount_price} lv.")
