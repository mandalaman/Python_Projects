# def factorial(number):
#     if number == 0 or number == 1:
#         return 1
#     else:
#         return number * factorial(number-1)
#
#
# if __name__ == '__main__':
#     number = int(input("Enter the number: "))
#     fac = factorial(number)
#     print(f"factorial is {fac}")

#No of Trailling zeros in a factorial

def trailing_factorial(number):
    count = 0
    while number>= 5:
        number //= 5
        count += number

    return count



if __name__ == '__main__':
    number = int(input("Enter the number: "))
    print(f"the factorialtrailingzero is", trailing_factorial(number))
