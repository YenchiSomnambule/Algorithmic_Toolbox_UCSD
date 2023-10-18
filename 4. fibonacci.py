from functools import lru_cache
@lru_cache(maxsize=None)  # Cache results for all calls


def fibonacci_number(n):
    if 0 <= n <= 45:
        if n <= 1:
            return n

        return fibonacci_number(n - 1) + fibonacci_number(n - 2)
    return('please set input within 0 to 45')


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
