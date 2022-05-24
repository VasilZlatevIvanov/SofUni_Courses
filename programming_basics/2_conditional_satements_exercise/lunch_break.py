import math

serial_name = input()
time_serial = int(input())
time_break = int(input())

launch_time = time_break * 1/8
spare_time = time_break * 1/4

total_break_time = launch_time + spare_time + time_serial

left_time = abs(time_break - total_break_time)
left_time = math.ceil(left_time)

if time_break >= total_break_time:
    print(f"You have enough time to watch {serial_name} and left with {left_time} minutes free time.")
elif time_break < total_break_time:
    print(f"You don't have enough time to watch {serial_name}, you need {left_time} more minutes.")

