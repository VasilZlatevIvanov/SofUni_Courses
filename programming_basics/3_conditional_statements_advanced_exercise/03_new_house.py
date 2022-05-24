flower_kind = input()
qty_flowers = int(input())
budget = int(input())

price = 0

if flower_kind == "Roses":
    price = 5
    if qty_flowers > 80:
        price *= 0.9
elif flower_kind == "Dahlias":
    price = 3.8
    if qty_flowers > 90:
        price *= 0.85
elif flower_kind == "Tulips":
    price = 2.80
    if qty_flowers > 80:
        price *= 0.85
elif flower_kind == "Narcissus":
    price = 3
    if qty_flowers < 120:
        price *= 1.15
elif flower_kind == "Gladiolus":
    price = 2.5
    if qty_flowers < 80:
        price *= 1.20

end_price = qty_flowers * price
result = abs(budget - end_price)
if budget >= end_price:
    print(f"Hey, you have a great garden with {qty_flowers} {flower_kind} and {result:.2f} leva left.")
elif budget < end_price:
    print(f"Not enough money, you need {result:.2f} leva more.")


