def sum_of_squares(upper_val):
    """

    :param upper_val:
    :return:
    """
    sum_val = 0

    for i in range(1,upper_val+1):
        sum_val += i*i

    return sum_val


def square_of_sum(upper_val):
    """

    :param upper_val:
    :return:
    """
    sum_val = 0

    for i in range(1,upper_val+1):
        sum_val += i

    return sum_val*sum_val


upper_val = 100

print(square_of_sum(upper_val)-sum_of_squares(upper_val))