def is_prime(num):
    """
    This function checks if a number is prime
    :param num:
    :return: bool
    """
    for i in range(2,num):
        if num % i == 0:
            return False

    return True

def test_concat_prime(val1, val2):
    """
    This function checks if the concatenation of two numbers (either order) is prime
    :param val1:
    :param val2:
    :return:
    """

    concat_val1 = int(str(val1)+str(val2))
    concat_val2 = int(str(val2)+str(val1))

    if is_prime(concat_val1) and is_prime(concat_val2):
        return True
    else:
        return False

def create_prime_list(num_of_vals):
    """
    This function creates a list of prime numbers the length of the provided value
    :param num_of_vals:
    :return:
    """
    list_full = False
    test_val = 2
    val_list = []

    while not list_full:
        if is_prime(test_val):
            val_list.append(test_val)
        if len(val_list) == num_of_vals:
            list_full = True
        test_val += 1

    return val_list


prime_list_index = 0
sum_of_list_vals = 0
prime_list_length = 1000
final_list_length = 5

prime_list = create_prime_list(prime_list_length)
final_list = []
test_list = [prime_list[0]]
concat_pair = True

while prime_list_index < (prime_list_length - final_list_length):
    for i in prime_list:
        print(i)
        for j in test_list:
            if not test_concat_prime(j, i):
                concat_pair = False
                print(j)
                break
            print(j)
        if concat_pair:
            test_list.append(i)
            if len(test_list) == final_list_length:
                break
        else:
            concat_pair = True
        print(test_list)
    if len(test_list) == final_list_length:
        break
    else:
        prime_list_index += 1
        del prime_list[0]
        if prime_list == final_list:
            break
        test_list = [prime_list[0]]


print(test_list)

