def is_palindrome(val):
    """

    :param val:
    :return:
    """
    if str(val) == str(val)[::-1]:
        return True
    else:
        return False


first_num_start = 999
second_num_start = 999
lrg_palindrome = 0

for num1 in range(first_num_start,0,-1):
    for num2 in range(second_num_start,0,-1):
        if is_palindrome(num1*num2):
            if num1*num2 > lrg_palindrome:
                lrg_palindrome = num1*num2
    first_num_start -= 1
    second_num_start -= 1


print(lrg_palindrome)
