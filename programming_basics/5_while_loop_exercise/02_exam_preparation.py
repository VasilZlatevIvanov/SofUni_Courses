failed_number_grade = int(input())
task_name = input()

count_bad_grade = 0
reached_number_bad_grades = False
count_grades = 0
sum_grades = 0

while task_name != "Enough":
    grade = int(input())
    if grade <= 4:
        count_bad_grade += 1
        count_grades += 1
        sum_grades += grade
    else:
        count_grades += 1
        sum_grades += grade
        last_task = task_name
    if count_bad_grade >= failed_number_grade:
        reached_number_bad_grades = True
        last_task = task_name
        break
    task_name = input()

avg_grade = sum_grades / count_grades


if reached_number_bad_grades:
    print(f"You need a break, {count_bad_grade} poor grades.")
else:
    print (f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {count_grades}")
    print(f"Last problem: {last_task}")
