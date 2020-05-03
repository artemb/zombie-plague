OBSTACLES = []
WALLS = []

def rect_obstacle(top_left, width, height):
    result = []

    for col in range(width):
        for row in range(height):
            result.append((top_left[0] + col, top_left[1] + row))

    return result

def hwall(top_left, length):
    result = []

    for col in range(length):
        result.append(((top_left[0] + col, top_left[1] - 1), (top_left[0] + col, top_left[1])))

    return result

def vwall(top_left, length):
    result = []

    for row in range(length):
        result.append(((top_left[0] - 1, top_left[1] + row), (top_left[0], top_left[1] + row)))

    return result

# The car
OBSTACLES += rect_obstacle((5, 3), 5, 3)

# The garage
OBSTACLES += rect_obstacle((15, 2), 6, 1)
OBSTACLES += rect_obstacle((16, 3), 1, 1)
OBSTACLES += rect_obstacle((20, 3), 1, 4)
OBSTACLES += [(18, 5), (15, 6)]
OBSTACLES += rect_obstacle((17, 6), 3, 1)

# Rocks and bushes
OBSTACLES += [
    (3, 7), (21, 2), (23, 7), (21, 9), (7, 9), (7, 10), (6, 10), (5, 10), (5, 11), (3, 11),
    (3, 14), (3, 16), (3, 20), (4, 20), (24, 13), (19, 14), (19, 15), (24, 20), (24, 19), (23, 20)
]

# Living room
OBSTACLES += rect_obstacle((8, 9), 4, 1)
OBSTACLES += [(10, 12), (11, 12), (11, 13), (13, 9), (13, 11)]
OBSTACLES += rect_obstacle((10, 15), 4, 1)

# Kitchen
OBSTACLES += rect_obstacle((8, 15), 1, 2)
OBSTACLES += rect_obstacle((8, 19), 5, 1)
OBSTACLES += rect_obstacle((11, 16), 1, 3)

# Bathroom
OBSTACLES += rect_obstacle((12, 16), 1, 2)
OBSTACLES += rect_obstacle((12, 19), 2, 1)

# Study
OBSTACLES += rect_obstacle((15, 15), 1, 4)
OBSTACLES += rect_obstacle((15, 19), 3, 1)
OBSTACLES += rect_obstacle((18, 17), 1, 3)
OBSTACLES += [(17, 14), (18, 14), (18, 15)]

# Bedroom
OBSTACLES += rect_obstacle((14, 9), 1, 3)
OBSTACLES += rect_obstacle((16, 9), 3, 2)
OBSTACLES += rect_obstacle((16, 13), 3, 1)


# Garage walls
# - all garage walls have obstactles next to them, so can skip

# House walls. Again, most are blocked by obstacles anyway
WALLS += hwall((13, 9), 6)
WALLS += vwall((19, 9), 3)
WALLS += vwall((8, 13), 1)

# Internal walls
WALLS += vwall((14, 9), 5)
WALLS += hwall((14, 12), 1)
WALLS += hwall((15, 14), 4)
WALLS += vwall((15, 15), 5)
WALLS += vwall((13, 15), 5)
WALLS += vwall((14, 15), 1)
WALLS += hwall((13, 16), 1)
