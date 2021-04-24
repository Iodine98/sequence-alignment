def prime(number):
    if number < 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


prime(3)
print(prime(5))
assert prime(7)
