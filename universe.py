def is_cross(list_1, list_2):
    sum_x = abs(list_1[2] - list_1[0]) + abs(list_2[2] - list_2[0])
    sum_y = abs(list_1[3] - list_1[1]) + abs(list_2[3] - list_2[1])

    x_min = min(list_1[0], list_1[2], list_2[0], list_2[2])
    x_max = max(list_1[0], list_1[2], list_2[0], list_2[2])
    y_min = min(list_1[1], list_1[3], list_2[1], list_2[3])
    y_max = max(list_1[1], list_1[3], list_2[1], list_2[3])

    return ((x_max - x_min) <= sum_x and (y_max - y_min) <= sum_y)
