class Addsub:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Sa main program(which is an Addsub)
calculator = Addsub(10, 5)
print("Addition:", calculator.add())            # Sa def add
print("Subtraction:", calculator.subtract())    # Sa def subtract

# Sa def calculate_sum ini
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = calculate_sum(numbers)
print("Sum of numbers:", sum_of_numbers)

# Counting the number if it is no.3
x = 0
while x < 5:
    print("Count:", x)
    if x == 3:
        print("Count is 3")
    else:
        print("Count is not 3")
    x += 1