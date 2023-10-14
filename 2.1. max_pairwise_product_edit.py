def max_pairwise_product(numbers):
    # Handle cases with less than two numbers
    if len(numbers) < 2:
        return 0

    # Initialize the two largest numbers
    max_num1 = max(numbers[0], numbers[1])
    max_num2 = min(numbers[0], numbers[1])

    # Traverse the list starting from the third number
    for num in numbers[2:]:
        if num > max_num1:
            max_num2 = max_num1
            max_num1 = num
        elif num > max_num2:
            max_num2 = num

    return max_num1 * max_num2

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
