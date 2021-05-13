def checkOverlap(radius, x_center, y_center, x1, y1, x2, y2):
    def distance(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    for x in [x1, x2]:
        for y in [y1, y2]:
            if distance(x_center, y_center, x, y) < radius:
                return True
    return ((x_center + radius < x1 or x2 < x_center - radius) and (
                y_center + radius < y1 or y2 < y_center - radius))


print(checkOverlap(1, 1, 1, 1, -3, 2, -1))
