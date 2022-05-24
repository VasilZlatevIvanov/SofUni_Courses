budget = float(input())
count_nights = int(input())
price_per_night = float(input())
percent_expenses = int(input())

if count_nights > 7:
    price_per_night = price_per_night * 0.95
else:
    pass
price_all_nights = count_nights * price_per_night
additional_expenses = budget * (percent_expenses / 100)
total_price = price_all_nights + additional_expenses
difference = abs(budget - total_price)
if budget >= total_price:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")

