count_of_groups = int(input())

groups_musala = 0
groups_monblan = 0
groups_kilimandjaro = 0
groups_k2 = 0
groups_everest = 0

for number in range(count_of_groups):
    current_group = int(input())
    if current_group <= 5:
        groups_musala += current_group
    elif current_group > 5 and current_group <= 12:
        groups_monblan += current_group
    elif current_group > 12 and current_group <= 25:
        groups_kilimandjaro += current_group
    elif current_group > 25 and current_group <= 40:
        groups_k2 += current_group
    elif current_group > 40:
        groups_everest += current_group

total_people = groups_musala + groups_monblan + groups_kilimandjaro + groups_k2 + groups_everest
percentage_musala = groups_musala / total_people * 100
percentage_monblan = groups_monblan / total_people * 100
percentage_kilimandjaro = groups_kilimandjaro / total_people * 100
percentage_k2 = groups_k2 / total_people * 100
percentage_everest = groups_everest / total_people * 100

print(f"{percentage_musala:.2f}%")
print(f"{percentage_monblan:.2f}%")
print(f"{percentage_kilimandjaro:.2f}%")
print(f"{percentage_k2:.2f}%")
print(f"{percentage_everest:.2f}%")
