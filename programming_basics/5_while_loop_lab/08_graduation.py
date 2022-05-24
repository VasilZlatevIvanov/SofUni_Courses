student_name = input()

year = 1
summ = 0
fail_count = 0
while year <= 12:
    if fail_count > 1:
        break

    grade = float(input())
    if grade < 4:
        fail_count += 1
        continue
    summ += grade
    year += 1

if fail_count > 1:
    print(f"{student_name} has been excluded at {year} grade")
else:
    avg_grade = summ / 12
    print(f"{student_name} graduated. Average grade: {avg_grade:.2f}")
