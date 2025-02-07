def smart_divider(f):
    def inner(num1, num2):
        if num2 == 0:
            print("can't not divided by zero!")
            return
        f(num1, num2)
    return inner
@smart_divider
def Divsion(num1, num2):
    print("Division is:", num1/num2)

Divsion(10, 0)

print("hellow ")

