k_range = int(input())
l_range = int(input())
m_range = int(input())
n_range = int(input())
count = 0

for k in range(k_range, 8 + 1):
    if k % 2 != 0:
        continue
    for l in range(9, l_range-1, -1):
        if l % 2 == 0:
            continue
        for m in range(m_range, 8 + 1):
            if m % 2 != 0:
                continue
            for n in range(9, n_range-1, -1):
                if n % 2 == 0:
                    continue
                if count >= 6:
                    break
                if k == m and l == n:
                    print(f"Cannot change the same player.")
                else:
                    count += 1
                    print(f"{k}{l} - {m}{n}")

print()