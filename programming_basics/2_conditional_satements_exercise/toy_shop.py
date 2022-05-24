price_for_excursion = float(input())
count_puzzles = int(input())
count_dolls = int(input())
count_bears = int(input())
count_minions = int(input())
count_trucks = int(input())

price_puzzle = 2.60
price_dolls = 3
price_bear = 4.10
price_minion = 8.20
price_truck = 2

total_puzzle = count_puzzles * price_puzzle
total_dolls = count_dolls * price_dolls
total_bear = count_bears * price_bear
total_minion = count_minions * price_minion
total_truck = count_trucks * price_truck

total_toys = count_puzzles + count_dolls + count_bears + count_minions + count_trucks
total_check = total_puzzle + total_dolls + total_bear + total_minion + total_truck

if total_toys >= 50:
    total_check *= 0.75
else:
    total_check *= 1

rent = total_check * 0.1
left_money = abs(price_for_excursion - (total_check - rent))

if total_check - rent >= price_for_excursion:
    print(f"Yes! {left_money:.2f} lv left.")
else:
    print(f"Not enough money! {left_money:.2f} lv needed.")