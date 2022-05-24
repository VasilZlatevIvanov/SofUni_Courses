width = int(input())
length = int(input())
height = int(input())
there_is_more_free_space = True
total_volume = width * length * height
command = input()
total_boxes = 0
space_left = 0

while command != "Done":
    number_of_boxes = int(command)
    total_boxes += number_of_boxes
    space_left = total_volume - total_boxes
    if space_left <= 0:
        there_is_more_free_space = False
        break
    command = input()
if there_is_more_free_space:
    print(f"{space_left} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(space_left)} Cubic meters more.")
