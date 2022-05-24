length = int(input())
width = int(input())
height = int(input())
percentage = float(input())
aquarium_volume = length * width * height
aquarium_volume_in_litres = aquarium_volume * 0.001
needed_litres_of_water = aquarium_volume_in_litres - (aquarium_volume_in_litres * percentage / 100)
print(needed_litres_of_water)
