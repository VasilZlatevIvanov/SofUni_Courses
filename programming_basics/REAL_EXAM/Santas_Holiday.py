vacancy_days = int(input())
kind_of_room = input()
rating = input()

# price_room_for_one_person = 18.00
# price_apartment = 25.00
# price_president_apartment = 35.00

price = 0
qty_nights = vacancy_days - 1

if kind_of_room == "room for one person":
    price = 18.00
elif kind_of_room == "apartment":
    price = 25.00
    if vacancy_days < 10:
        price *= 0.7
    elif vacancy_days >= 10 and vacancy_days <= 15:
        price *= 0.65
    elif vacancy_days > 15:
        price *= 0.5
elif kind_of_room == "president apartment":
    price = 35.00
    if vacancy_days < 10:
        price *= 0.9
    elif vacancy_days >=  10 and vacancy_days <= 15:
        price *= 0.85
    elif vacancy_days > 15:
        price *= 0.8

staying_price = price * qty_nights

if rating == "positive":
    staying_price *= 1.25
elif rating == "negative":
    staying_price *= 0.9

print(f"{staying_price:.2f}")

price_room_for_one_person = 18.00
price_apartment = 25.00
price_president_apartment = 35.00
