import time
from typing import Optional
from tqdm import tqdm
from primefac import primefac


def find_prime_factors(n, prime_factors=[]):
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        prime_factors.append(n)
    return prime_factors


def optimized_find_prime_factors(
    n: int, prime_factors: Optional[list] = None
) -> list[int]:
    """
    Finds all prime factors for a given integer

    :param n: The integer whose factors are to be found
    :param prime_factors: The list used to store the integers, if the user wishes to pass their own
    :return: A list containing all prime factors of the number passed
    """
    if prime_factors is None:
        prime_factors = []

    # if n == 0 or n == 1 we can just skip everything and return
    if n < 2:
        return prime_factors

    # remove all even numbers from the list
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2

    i = 3

    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 2

    if n > 1:
        prime_factors.append(n)

    return prime_factors


def test_find_prime_factors() -> None:
    """
    Ensure that the original function and its optimized version produce the same results, as well
    as testing their speed over 1_000_000 iterations
    """
    print(
        """
********************************************
Ensure that the results returned are correct
********************************************
"""
    )

    for i in tqdm(range(1_000_000)):
        assert find_prime_factors(i, []) == list(primefac(i))

    i = 1_000_000
    while i <= 1_000_000_000_000:
        assert find_prime_factors(i, []) == list(primefac(i))
        i *= 10

    print(
        """
*******************************************
Test both functions return the same answers
*******************************************
"""
    )
    for i in tqdm(range(1_000_000)):
        assert find_prime_factors(i, []) == optimized_find_prime_factors(i)

    i = 1_000_000
    while i <= 1_000_000_000_000:
        assert find_prime_factors(i, []) == optimized_find_prime_factors(i)
        i *= 10

    print(
        """
**************************
Completed correctness test
**************************
"""
    )

    print(
        """
*********************
Test time performance
*********************
"""
    )

    start_time = time.time()

    for i in tqdm(range(1_000_000)):
        find_prime_factors(i, [])

    end_og_func_time = time.time()

    for i in tqdm(range(1_000_000)):
        optimized_find_prime_factors(i)

    end_optimized_func_time = time.time()

    print(
        f"""Original function executed 1_000_000 iterations in {end_og_func_time-start_time:.2f}s.
Optimized function executed 1_000_000 iterations in {end_optimized_func_time-end_og_func_time:.2f}s
"""
    )

    print(
        """
*******************
Completed time test
*******************
"""
    )


def main() -> None:
    print(list(primefac(1000)))
    print(find_prime_factors(1000))
    test_find_prime_factors()


if __name__ == "__main__":
    main()
