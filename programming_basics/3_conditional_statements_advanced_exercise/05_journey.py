budget = float(input())
season = input()

price = 0

if budget <= 100 and season == "summer":
    price = budget * 0.3
    print("Somewhere in Bulgaria")
    print(f"Camp - {price:.2f}")
elif budget <= 100 and season == "winter":
    price = budget * 0.7
    print("Somewhere in Bulgaria")
    print(f"Hotel - {price:.2f}")
elif budget <= 1000 and season == "summer":
    price = budget * 0.4
    print("Somewhere in Balkans")
    print(f"Camp - {price:.2f}")
elif budget <= 1000 and season == "winter":
    price = budget * 0.8
    print("Somewhere in Balkans")
    print(f"Hotel - {price:.2f}")
elif budget > 1000 and season == "summer":
    price = budget * 0.9
    print("Somewhere in Europe")
    print(f"Hotel - {price:.2f}")
elif budget > 1000 and season == "winter":
    price = budget * 0.9
    print("Somewhere in Europe")
    print(f"Hotel - {price:.2f}")
