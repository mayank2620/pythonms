floor_length = float(input("Enter the length of the floor: "))
floor_width = float(input("Enter the width of the floor: "))
tile_length = float(input("Enter the length of a tile: "))
tile_width = float(input("Enter the width of a tile: "))


num_tiles_length = int(floor_length / tile_length)
num_tiles_width = int(floor_width / tile_width)
num_tiles_required = num_tiles_length * num_tiles_width


print("The number of tiles required is:", num_tiles_required)