#python program that show the odd and even number

def odd_or_even(numbers):
    odd_num = []
    even_num = []

    for num in numbers:
        if num % 2  == 0:
            even_num.append(num)
        else:
            odd_num.append(num)

    return odd_num, even_num

number_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
odds, even = odd_or_even(number_list)

print("Odd numbers:", odds)
print("Even numbers:", even)

def countdown(start_num):
    while start_num >= 0:
        print(start_num)
        start_num -= 1

        print("Countdown Timer")

initial_num = int(input("Enter the starting number: "))

print("Countdown starts: ")
countdown(initial_num)
print("Countdown Finished!")
    