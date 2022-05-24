month = input()
qty_of_nights = int(input())

kind = ""
studio_price = 0
apartment_price = 0

#•	На първия ред е месецът - May, June, July, August, September или October;
if month == "May" or month == "October":
    if qty_of_nights <= 7:
        studio_price = 50
        apartment_price = 65
    elif 7 < qty_of_nights <= 14:
        studio_price = 50 - 50 * 0.05
        apartment_price = 65
    elif qty_of_nights > 14:
        studio_price = 50 - 50 * 0.30
        apartment_price = 65 - 65 * 0.10

elif month == "June" or month == "September":
    if qty_of_nights <= 14:
        studio_price = 75.20
        apartment_price = 68.70
    elif qty_of_nights > 14:
        studio_price = 75.20 - 75.20 * 0.20
        apartment_price = 68.70 - 68.70 * 0.10
elif month == "July" or month == "August":
    if qty_of_nights <= 14:
        studio_price = 76
        apartment_price = 77
    elif qty_of_nights > 14:
        studio_price = 76
        apartment_price = 77 - 77 * 0.10

total_price_studio = qty_of_nights * studio_price
total_price_apartment = qty_of_nights * apartment_price
print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")
