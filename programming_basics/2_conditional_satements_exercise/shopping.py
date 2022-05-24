budget = float(input())
count_video_card = int(input())
count_processors = int(input())
count_ram = int(input())

price_video_card = 250
price_processors = price_video_card * count_video_card * 0.35
price_ram = price_video_card * count_video_card * 0.1

total_price = price_video_card * count_video_card + price_processors * count_processors + count_ram * price_ram


if count_video_card > count_processors:
    total_price *= 0.85

left_money = abs(budget - total_price)

if total_price <= budget:
    print(f"You have {left_money:.2f} leva left!")
elif total_price > budget:
    print(f"Not enough money! You need {left_money:.2f} leva more!")
