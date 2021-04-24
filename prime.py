from typing import List
import json
from datetime import datetime
from math import prod, log, factorial
from tqdm import tqdm
import sys


def dividing_counter(n: int, divisor: int, return_n=False):
    n_input = n
    counter = 0
    while n_input % divisor == 0:
        n_input //= divisor
        counter += 1
    if return_n:
        return n_input, counter
    return counter

    # def list_of_prime_numbers_to_n(n: int):
    #     prime_numbers_list = []
    #     max_range = n + 1
    #
    #     for i in tqdm(range(2, max_range), desc='Prime numbers'):
    #         is_prime = True
    #         stop = False
    #         for j in prime_numbers_list:
    #             if i % j == 0:
    #                 is_prime = False
    #                 break
    #             if n % j == 0:
    #                 exponent = dividing_counter(n, j)
    #                 stop = True if i >= n / j ** exponent else False
    #         if is_prime:
    #             prime_numbers_list.append(i)
    #         if stop:
    #             break
    #     return prime_numbers_list


def is_prime_given_list(i: int, numbers: list) -> bool:
    for j in numbers:
        if i % j == 0:
            return False
    return True


def list_of_prime_numbers_to_n(n: int):
    prime_numbers_list = []
    max_range = n + 1
    i = 2
    pbar = tqdm(
        total=max_range, initial=i, position=0, unit_scale=True, desc="Prime numbers"
    )
    while i < max_range:
        if (i == 2 or i % 2 == 1) and is_prime_given_list(i, prime_numbers_list):
            if n % i == 0:
                exponent = dividing_counter(n, i)
                new_range = max_range // (i ** exponent) + 1
                if new_range < max_range:
                    max_range = new_range
                    pbar.close()
                    pbar = tqdm(
                        total=max_range,
                        initial=i,
                        position=0,
                        unit_scale=True,
                        desc="Prime numbers",
                    )
                prime_numbers_list.append(i)
        i += 1
        pbar.update(1)
    pbar.close()
    return prime_numbers_list


def is_prime_fn_treshold(n: int, likelihood=0):
    number_count = 0
    for i in range(2, n):
        if n % i == 0:
            return False
        if likelihood != 0 and likelihood < (number_count / (n - 3)):
            return True
    return True


def list_of_product_tuples_of_n(n: int, list_of_prime_numbers: List[int]):
    input_n = n
    product_tuples = []
    for prime_number in tqdm(list_of_prime_numbers, desc="Prime numbers list"):
        n, exponent = dividing_counter(n, prime_number, return_n=True)
        if exponent > 0:
            product_tuples.append((prime_number, exponent))
    if len(product_tuples) > 0:
        return product_tuples
    return product_tuples.append((input_n, 1))


if __name__ == "__main__":
    begin = datetime.now()
    input_number = factorial(30)
    product_tuples_list = [(input_number, 1)]
    if not is_prime_fn_treshold(input_number):
        prime_numbers = list_of_prime_numbers_to_n(input_number)
        product_tuples_list = list_of_product_tuples_of_n(input_number, prime_numbers)
    end = datetime.now()
    print(product_tuples_list)
    print(prod(t[0] ** t[1] for t in product_tuples_list))
    print(end - begin)
