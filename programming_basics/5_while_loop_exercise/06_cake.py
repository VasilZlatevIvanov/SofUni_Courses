width = int(input())
length = int(input())

total_cake_pieces = width * length
cake_is_over = False
command = input()
total_pieces = 0
cake_left = 0

while command != "STOP":
    current_piece = int(command)
    total_pieces += current_piece
    cake_left = total_cake_pieces - total_pieces
    if cake_left <= 0:
        cake_is_over = True
        break
    command = input()
cake_left = abs(cake_left)
if cake_is_over:
    print(f"No more cake left! You need {cake_left} pieces more.")
else:
    print(f"{cake_left} pieces are left.")