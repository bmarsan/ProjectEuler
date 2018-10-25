"""
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally)
in the 20×20 grid?
"""

import re


def string_to_list(string_nums):
    """
    This function converts the provided string to a list of lists.
    :param string:
    :return:
    """
    final_list = []
    temp_list = []

    comma_list = string_nums.split("\n")

    for i in comma_list:
        for j in i.split(' '):
            temp_list.append(int(j))
        final_list.append(temp_list)
        temp_list = []

    return final_list


def calculate_prodcut(num_list):
    """
    This function will find the product of the values in the provided list.
    :param num_list:
    :return:
    """
    prodcut_val = 1

    for i in num_list:
        prodcut_val *= i

    return prodcut_val


def find_right_left_max(data_set, count):
    """
    This function will find the largest product of adjacent (left to right) numbers in the dataset.
    :param data_set:
    :return:
    """
    row_index = 0
    first_index = 0
    last_index = first_index + (count - 1)
    temp_first_index = first_index
    temp_last_index = last_index
    max_product_val = 0
    max_vals = []

    while row_index < len(data_set):
        while temp_last_index < len(data_set[row_index]):
            temp_prod_val = calculate_prodcut(data_set[row_index][temp_first_index:temp_last_index+1])
            if temp_prod_val > max_product_val:
                max_product_val = temp_prod_val
                max_vals = data_set[row_index][temp_first_index:temp_last_index+1]
                max_row = row_index
            temp_first_index += 1
            temp_last_index += 1
        row_index += 1
        temp_first_index = first_index
        temp_last_index = last_index

    print("Max right to left product: {0}".format(max_product_val))
    print("Max right to left row: {0}".format(max_row))
    print("Max right to left values: {0}".format(max_vals))


def find_up_down_max(data_set, count):
    """
    This function will find the largest product of adjacent (up and down) numbers.
    :param data_set:
    :param count:
    :return:
    """
    first_row_index = 0
    last_row_index = first_row_index + (count - 1)
    value_index = 0
    temp_val_list = []
    max_product_val = 0
    temp_product = 0

    while last_row_index < len(data_set):
        while value_index < len(data_set[first_row_index]):
            for i in range(first_row_index, last_row_index+1):
                temp_val_list.append(data_set[i][value_index])
            temp_product = calculate_prodcut(temp_val_list)
            if temp_product > max_product_val:
                max_product_val = temp_product
                max_vals = temp_val_list
                max_col = value_index
            temp_val_list = []
            value_index += 1
        first_row_index += 1
        last_row_index += 1
        value_index = 0

    print("Max up/down product: {0}".format(max_product_val))
    print("Max up/down row: {0}".format(max_col))
    print("Max up/down values: {0}".format(max_vals))


def find_diagonal_ltor_max(data_set, count):
    """
    Will find the max product of diagonal numbers scanning left to right.
    :param data_set:
    :param count:
    :return:
    """
    first_row_index = 0
    last_row_index = first_row_index + (count - 1)
    value_index = 0
    temp_value_index = value_index
    temp_val_list = []
    max_product_val = 0
    temp_product = 0

    while last_row_index < len(data_set):
        while value_index + (count - 1) < len(data_set[first_row_index]):
            for i in range(first_row_index, last_row_index+1):
                temp_val_list.append(data_set[i][temp_value_index])
                temp_value_index += 1
            temp_product = calculate_prodcut(temp_val_list)
            if temp_product > max_product_val:
                max_product_val = temp_product
                max_vals = temp_val_list
                max_row = first_row_index
            value_index += 1
            temp_value_index = value_index
            temp_val_list = []
        first_row_index += 1
        last_row_index += 1
        value_index = 0
        temp_value_index = 0

    print(max_product_val)
    print("Max diagonal product: {0}".format(max_product_val))
    print("Max diagonal row: {0}".format(max_row))
    print("Max diagonal values: {0}".format(max_vals))


def find_diagonal_rtol_max(data_set, count):
    """
    Will find the max product of diagonal numbers scanning right to left.
    :param data_set:
    :param count:
    :return:
    """
    first_row_index = 0
    last_row_index = first_row_index + (count - 1)
    value_index = len(data_set[0])-1
    temp_value_index = value_index
    temp_val_list = []
    max_product_val = 0
    temp_product = 0

    while last_row_index < len(data_set):
        while value_index - (count - 1) >= 0:
            for i in range(first_row_index, last_row_index+1):
                temp_val_list.append(data_set[i][temp_value_index])
                temp_value_index -= 1
            temp_product = calculate_prodcut(temp_val_list)
            if temp_product > max_product_val:
                max_product_val = temp_product
                max_vals = temp_val_list
                max_row = first_row_index
            value_index -= 1
            temp_value_index = value_index
            temp_val_list = []
        first_row_index += 1
        last_row_index += 1
        value_index = len(data_set[0])-1
        temp_value_index = value_index

    print(max_product_val)
    print("Max diagonal product: {0}".format(max_product_val))
    print("Max diagonal row: {0}".format(max_row))
    print("Max diagonal values: {0}".format(max_vals))

data_set_string = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

adjacent_count = 4

data_set = string_to_list(data_set_string)
find_right_left_max(data_set, adjacent_count)
find_up_down_max(data_set,adjacent_count)
find_diagonal_ltor_max(data_set, adjacent_count)
find_diagonal_rtol_max(data_set, adjacent_count)

