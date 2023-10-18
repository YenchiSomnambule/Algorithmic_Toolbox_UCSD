def pisano_period_length(m):
    previous, current = 0, 1
    for i in range(m * m):  # Pisano period for modulo m is at most m^2
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:  # Start of a new cycle
            return i + 1

def fibonacci_sum(n):
    if n <= 1:
        return n

    # Sum of n Fibonacci numbers is F[n+2] - 1 modulo 10
    length = pisano_period_length(10)
    n_new = (n + 2) % length
    if n_new == 0:
        return 9

    previous, current = 0, 1
    for _ in range(n_new - 1):
        previous, current = current, previous + current

    if current == 0:
        return 9
    else:
        return (current - 1) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))