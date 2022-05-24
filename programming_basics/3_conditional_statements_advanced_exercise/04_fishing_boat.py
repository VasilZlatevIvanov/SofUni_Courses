budget = int(input())
season = input()
number_of_fisherman = int(input())
boat_rent = 0

if season == "Spring":
    boat_rent = 3000
elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600

if number_of_fisherman <= 6:
    boat_rent *= 0.9
elif number_of_fisherman <= 11:
    boat_rent *= 0.85
elif number_of_fisherman >= 12:
    boat_rent *= 0.75

if season != "Autumn" and number_of_fisherman %2 == 0:
    boat_rent *= 0.95

difference = abs(boat_rent - budget)
if budget >= boat_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
elif budget < boat_rent:
    print(f"Not enough money! You need {difference:.2f} leva.")

