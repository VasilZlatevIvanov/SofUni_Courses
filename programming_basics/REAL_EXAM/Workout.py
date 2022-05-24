from math import ceil

count_days = int(input())
first_day_km = float(input())

sum_every_day_km = 0
current_day_km = first_day_km


for days in range (1, count_days + 1):
    every_day_km = int(input())
    every_day_km_transpose = (every_day_km + 100) / 100
    current_day_km *= every_day_km_transpose
    sum_every_day_km += current_day_km

total_km = first_day_km + sum_every_day_km
diff = abs(total_km - 1000)
if total_km >= 1000:
    print(f"You've done a great job running {ceil(diff)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(diff)} more kilometers")
