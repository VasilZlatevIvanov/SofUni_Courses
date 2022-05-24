# steps = input()
# sum_steps = 0
# final_goal = 10000
#
# while sum_steps <= final_goal:
#     if steps == "Going home":
#         steps = input()
#         sum_steps = sum_steps + int(steps)
#         break
#     else:
#         sum_steps = sum_steps + int(steps)
#         steps = input()
#
# diff = abs(10000 - sum_steps)
#
# if sum_steps >= 10000:
#     print(f"Goal reached! Good job!")
#     print(f"{diff} steps over the goal!")
# else:
#     print(f"{diff} more steps to reach goal.")


steps = input()
sum_steps = 0
target = 10000

while steps != "Going home":
    sum_steps += int(steps)
    if sum_steps >= target:
        break
    steps = input()

if steps == "Going home":
    steps = int(input())
    sum_steps += steps
else:
    pass

diff = abs(10000 - sum_steps)

if sum_steps >= 10000:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
