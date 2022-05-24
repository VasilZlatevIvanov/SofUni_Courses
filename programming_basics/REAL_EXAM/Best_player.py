name_of_player = input()
current_name = ""
current_goals = 0

while name_of_player != "END":
    count_goals = int(input())
    if count_goals > current_goals:
        current_name = name_of_player
        current_goals = count_goals
    if count_goals >= 10:
        break
    name_of_player = input()


if current_goals >= 3:
    print(f"{current_name} is the best player!")
    print(f"He has scored {current_goals} goals and made a hat-trick !!!")
else:
    print(f"{current_name} is the best player!")
    print(f"He has scored {current_goals} goals.")
