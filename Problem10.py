"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def sieve_of_eratosthenes(n):
    """
    This function will create a list of prime numbers (bools) up to the provided number.
    :param n:
    :return:
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

    return prime_list


def sum_of_list(prime_list,n):
    """
    This function finds the sum of the prime values (indexes) in the provided boolean list.
    :param n:
    :param prime_list:
    :return:
    """
    sum_of_list = 0

    for i in range(n):
        if prime_list[i]:
            sum_of_list += i

    return sum_of_list


n = 10

prime_list = sieve_of_eratosthenes(n)
print(sum_of_list(prime_list, n))