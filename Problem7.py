def sieve_of_eratosthenes(n):
    """
    Seive of Eratosthenes - This function will build a list of prime
    numbers up to the specified value.
    :param n:
    :return list:
    """
    prime_list = [True]*(n+1)
    prime_list[0] = False
    prime_list[1] = False

    p = 2

    while p * p <= n:
        if prime_list[p]:

            for i in range(2*p, n+1, p):
                prime_list[i] = False

        p += 1

    for i in range(2,n):
        if prime_list[i]:
            print(i)


def is_prime(num):
    """

    :param num:
    :return: bool
    """
    for i in range(2,num):
        if num % i == 0:
            return False

    return True


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


def nth_prime_number(n):
    # initial prime number list
    prime_list = [2]
    # first number to test if prime
    num = 3
    # keep generating primes until we get to the nth one
    while len(prime_list) < n:

        # check if num is divisible by any prime before it
        for p in prime_list:
            # if there is no remainder dividing the number
            # then the number is not a prime
            if num % p == 0:
                # break to stop testing more numbers, we know it's not a prime
                break

        # if it is a prime, then add it to the list
        # after a for loop, else runs if the "break" command has not been given
        else:
            # append to prime list
            prime_list.append(num)

        # same optimization you had, don't check even numbers
        num += 2

    # return the last prime number generated
    return prime_list[-1]


#sieve_of_eratosthenes(20)

#prime_list = create_prime_list(10002)
#print(prime_list[10000])

print(nth_prime_number(10001))