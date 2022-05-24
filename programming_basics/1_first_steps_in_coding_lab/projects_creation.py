#The architect {името на архитекта} will need {необходими часове} hours to complete
#{брой на проектите} project/s.

arch_name = input()
count_projects = int(input())
one_project_time = 3

calc_time = count_projects * one_project_time

print(f"The architect {arch_name} will need {calc_time} hours to complete {count_projects} project/s.")
