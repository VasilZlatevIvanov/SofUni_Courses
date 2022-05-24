import math

count_tour = int(input())
starting_points = int(input())

current_points = 0
wins = 0

for number in range(count_tour):
    outcome = input()
    if outcome == "W":
        current_points += 2000
        wins += 1
    elif outcome == "F":
        current_points += 1200
    elif outcome == "SF":
        current_points += 720

final_points = current_points + starting_points
avg_points = current_points / count_tour
rounded_down_avg_points = math.floor(avg_points)
percentage_wining = wins / count_tour * 100

# •	"Final points: {брой точки след изиграните турнири}"
# •	"Average points: {средно колко точки печели за турнир}"
# •	"{процент спечелени турнири}%"

print(f"Final points: {final_points}")
print(f"Average points: {rounded_down_avg_points}")
print(f"{percentage_wining:.2f}%")


