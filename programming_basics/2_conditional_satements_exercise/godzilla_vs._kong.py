budget = float(input())
number_of_statists = int(input())
one_dress_price = float(input())

decor = budget * 0.1
dress_price = number_of_statists * one_dress_price

if number_of_statists > 150:
    dress_price *= 0.9

needed_money = decor + dress_price
difference = abs(needed_money - budget)

if needed_money > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
elif needed_money <= budget:
    print(f"Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
