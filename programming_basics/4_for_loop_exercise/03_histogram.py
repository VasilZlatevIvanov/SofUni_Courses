count_of_numbers = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for number in range(count_of_numbers):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif current_number < 400:
        p2 += 1
    elif current_number < 600:
        p3 += 1
    elif current_number < 800:
        p4 += 1
    elif current_number >= 800:
        p5 += 1
percentage_p1 = p1 / count_of_numbers * 100
percentage_p2 = p2 / count_of_numbers * 100
percentage_p3 = p3 / count_of_numbers * 100
percentage_p4 = p4 / count_of_numbers * 100
percentage_p5 = p5 / count_of_numbers * 100

print(f"{percentage_p1:.2f}%")
print(f"{percentage_p2:.2f}%")
print(f"{percentage_p3:.2f}%")
print(f"{percentage_p4:.2f}%")
print(f"{percentage_p5:.2f}%")