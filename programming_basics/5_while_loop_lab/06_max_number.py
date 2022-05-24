import sys

line = input()

max_num = -sys.maxsize
while line != "Stop":
    current_num = int(line)

    if current_num > max_num:
        max_num = current_num

    line = input()

print(max_num)

