def find_sum(num, max_val):
    """

    :param num:
    :param max_val:
    :return: sum_val
    """
    sum_val = 0
    loop_val = int(max_val/num)

    if max_val & num == 0:
        loop_val -= 1

    for i in range(1,loop_val+1):
        sum_val += num*i

    return sum_val

def find_sum_list(val1, val2, upper_val):
    """

    :param val1:
    :param val2:
    :param upper_val:
    :return:
    """
    val_list = []
    sum_val = 0

    for i in range(1,upper_val):
        if i%val1 == 0 or i%val2 == 0:
            val_list.append(i)

    for val in val_list:
        sum_val += val

    return sum_val


sum_val1 = find_sum(3,1000)
sum_val2 = find_sum(5,1000)

print(sum_val1+sum_val2)

print(find_sum_list(3,5,1000))