first_player_eggs = int(input())
second_player_eggs = int(input())
command = input()
count_first_player_eggs = first_player_eggs
count_second_player_eggs = second_player_eggs

while command != "End of battle":
    if command == "one":
        count_second_player_eggs -= 1
    elif command == "two":
        count_first_player_eggs -= 1
    if count_second_player_eggs == 0 or count_first_player_eggs == 0:
        break
    command = input()
if count_first_player_eggs == 0:
    print(f"Player one is out of eggs. Player two has {count_second_player_eggs} eggs left.")
elif count_second_player_eggs == 0:
    print(f"Player two is out of eggs. Player one has {count_first_player_eggs} eggs left.")
else:
    print(f"Player one has {count_first_player_eggs} eggs left.")
    print(f"Player two has {count_second_player_eggs} eggs left.")
