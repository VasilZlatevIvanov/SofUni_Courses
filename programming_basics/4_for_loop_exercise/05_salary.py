count_open_tabs = int(input())
salary = float(input())

total_amount = salary

for name in range(1, count_open_tabs + 1):
    current_name = input()
    if total_amount <= 0:
        break
    if current_name == "Facebook":
        total_amount -= 150
    elif current_name == "Instagram":
        total_amount -= 100
    elif current_name == "Reddit":
        total_amount -= 50
    else:
        total_amount -= 0

if total_amount <= 0:
    print("You have lost your salary.")
elif total_amount > 0:
    print(f"{total_amount:.0f}")
