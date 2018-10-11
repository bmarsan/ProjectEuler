def is_prime(num):
    """

    :param num:
    :return: bool
    """
    for i in range(2,num):
        if num % i == 0:
            return False

    return True


largest_prime = 0
total_val = 600851475143

for val in range(2,total_val):
    if total_val % val == 0:
        if is_prime(int(total_val/val)):
            largest_prime = int(total_val/val)
            break

if largest_prime == 0:
    print("No prime factor")
else:
    print(largest_prime)
