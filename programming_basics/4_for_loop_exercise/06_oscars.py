actor_name = input()
total_points = float(input())
number_of_jury = int(input())
for current_grade in range(number_of_jury):
    current_name = input()
    current_points = float(input())
    current_final_points = len(current_name) * current_points / 2
    total_points += current_final_points
    if total_points > 1250.5:
        break
if total_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    diff = abs(1250.5 - total_points)
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")

