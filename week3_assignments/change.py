def change(money):
    # write your code here
    count = 0
    while money > 0:
        count += 1
        if money >= 10:
            money -= 10
        elif 5 <= money < 10:
            money -= 5
        elif 1 <= money < 5:
            money -= 1

    return count


#amount = 28
#coins_needed = change(amount)
#print(f"For {amount} units, you need {coins_needed} coins.")


if __name__ == '__main__':
    m = int(input())
    print(change(m))
