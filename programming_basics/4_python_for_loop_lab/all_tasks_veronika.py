# 01. Numbers from 1 to 100

for i in range(1, 101):
    print(i)

# 02. Numbers 1...N with Step 3

number = int(input())

for i in range(1, number + 1, 3):
    print(i)

# 03. Even Powers of 2

n = int(input())

num = 1
for degree in range(0, n + 1, 2):
    print(2 ** degree)
    # print(num)
    # num = num * 2 * 2

# 04. Numbers N...1

n = int(input())

for i in range(n, 0, -1):
    print(i)

# 05. Character Sequence

text = input()

len_text = len(text)
for i in range(0, len_text):
    print(text[i])


text = input()

for char in text:
    print(char)

# 06.
text = input()

len_text = len(text)
sum = 0
for letter in text:
    if letter == 'a':
        sum += 1
    elif letter == 'e':
        sum += 2
    elif letter == 'i':
        sum += 3
    elif letter == 'o':
        sum += 4
    elif letter == 'u':
        sum += 5

print(sum)

# 07. Sum Numbers


n = int(input())

sum = 0
for i in range(1, n + 1):
    value = int(input())
    sum += value

print(sum)

# 08. Number sequence

import sys

n = int(input())
max_num = -sys.maxsize
min_num = sys.maxsize
for i in range(1, n + 1):
    value = int(input())
    if value > max_num:
        max_num = value
    if value < min_num:
        min_num = value

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")


# 09. Left and Right Sum

n = int(input())

left_sum = 0
right_sum = 0
for i in range(1, n + 1):
    value = int(input())
    left_sum += value

for i in range(1, n + 1):
    value = int(input())
    right_sum += value

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum-right_sum)}")

# 10. Odd Even Sum

n = int(input())

even_sum = 0
odd_sum = 0
for i in range(1, n + 1):
    value = int(input())
    if i % 2 == 0:
        even_sum += value
    else:
        odd_sum += value

if even_sum == odd_sum:
    print(f"Yes, sum = {odd_sum}")
else:
    print(f"No, diff = {abs(even_sum-odd_sum)}")
