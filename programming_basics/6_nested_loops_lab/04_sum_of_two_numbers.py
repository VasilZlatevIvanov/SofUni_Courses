start = int(input())
end = int(input())
magic_num = int(input())

flag = False
count = 0
for x in range(start, end + 1):
    for y in range(start, end + 1):
        sum = x + y
        count += 1
        if sum == magic_num:
            print(f"Combination N:{count} ({x} + {y} = {sum})")
            flag = True
            break
    if flag:
        break
if not flag:
    print(f"{count} combinations - neither equals {magic_num}")