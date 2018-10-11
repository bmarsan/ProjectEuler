def is_evenly_divisible(num):
    """

    :param num:
    :return:
    """

    for i in range(11,21):
        if num%i != 0:
            return False

    return True


test_val = 0
is_divisible = False

while not is_divisible:
    test_val += 20
    is_divisible = is_evenly_divisible(test_val)

print(test_val)




