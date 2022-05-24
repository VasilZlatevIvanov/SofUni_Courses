fruit = input()
day_of_week = input()
qty = float(input())

price = 0

is_fruit = fruit == "banana" \
           or fruit == "apple" \
           or fruit == "orange" \
           or fruit == "grapefruit" \
           or fruit == "kiwi" \
           or fruit == "pineapple" \
           or fruit == "grapes"
is_day_of_week = day_of_week == "Monday" \
                 or day_of_week == "Tuesday" \
                 or day_of_week == "Wednesday" \
                 or day_of_week == "Thursday" \
                 or day_of_week == "Friday" \
                 or day_of_week == "Saturday" \
                 or day_of_week == "Sunday"

if is_fruit and is_day_of_week:
    if day_of_week == "Monday" \
            or day_of_week == "Tuesday" \
            or day_of_week == "Wednesday" \
            or day_of_week == "Thursday" \
            or day_of_week == "Friday":
        if fruit == "banana":
            price = 2.50
        elif fruit == "apple":
            price = 1.20
        elif fruit == "orange":
            price = 0.85
        elif fruit == "grapefruit":
            price = 1.45
        elif fruit == "kiwi":
            price = 2.70
        elif fruit == "pineapple":
            price = 5.50
        elif fruit == "grapes":
            price = 3.85
    elif day_of_week == "Saturday" or day_of_week == "Sunday":
        if fruit == "banana":
            price = 2.70
        elif fruit == "apple":
            price = 1.25
        elif fruit == "orange":
            price = 0.90
        elif fruit == "grapefruit":
            price = 1.60
        elif fruit == "kiwi":
            price = 3.00
        elif fruit == "pineapple":
            price = 5.60
        elif fruit == "grapes":
            price = 4.20
    print(f"{qty * price:.2f}")
else:
    print("error")



