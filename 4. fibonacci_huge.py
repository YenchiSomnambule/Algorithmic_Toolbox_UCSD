def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        if (previous, current) == (0, 1):
            return i + 1

def fibonacci_huge(n, m):
    remainder = n % pisano_period(m)
    first, second = 0, 1
    res = remainder

    for _ in range(1, remainder):
        first, second = second, first + second
        res = second % m

    return res % m

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))