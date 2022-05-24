hour = int(input())
day = input()


is_working_day = day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday"
is_day_off = day == "Sunday"
if hour >= 10 and hour <= 18:
    if is_working_day:
        print("open")
    elif is_day_off:
        print("closed")

if hour < 10 or hour > 18:
    if is_working_day:
        print("closed")
    elif is_day_off:
        print("closed")
