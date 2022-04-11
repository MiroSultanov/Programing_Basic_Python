width = int(input())
length = int(input())
height = int(input())
total_volume = width * length * height
is_there_more_free_space = True
command = input()
while command != "Done":
    number_of_boxes = int(command)
    total_volume -= number_of_boxes
    if total_volume < 0:
        is_there_more_free_space = False
        break
    command = input()
if is_there_more_free_space:
    print(f"{total_volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(total_volume)} Cubic meters more.")