def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result < 2:
            print('Составное')  # Числа < 2 не являются простыми
            return result

        is_primes = True
        for i in range(2, int(result ** 0.5) + 1):
            if result % i == 0:
                is_primes = False
                break

        if is_primes:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)