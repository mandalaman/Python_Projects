# #Mutable
# lst = [1, 2, 3]
# lst[0] = 10

# print(lst)

# #immutable

# tpl = (1,3,4)
# #tpl[0] = 5
# print(tpl)

# x = [1,2,3]
# y = [1,2,3]

# z = x

# print(x==y)
# print(x is y)
# print(x is z)

# import threading

# def task():
#     print("task excuted.")


# thread = threading.Thread(target= task)
# thread.start()
# thread.join()

# def decorator(func):
#     def wrapper():
#         print("Before fuction call")
#         func()
#         print("after function call")

#     return wrapper
# @decorator
# def greet():
#     print("Hello!")

# greet()


# #List Comprehensions
# square = [x**2 for x in range(6)]
# print(square)

# #set comprehensions

# unique = {x for x in [1,2,3,3,4]}
# print(unique)

# #dict comprehensions

# square_dict = {x:x**2 for x in range(4)}
# print(square_dict)
# import copy
# lst = [[1,2], [3,4]]

# shallow = copy.copy(lst)
# shallow[0][0] = 10

# print(lst)
# lst = [[1,2], [3,4]]
# deep = copy.deepcopy(lst)
# deep[0][0] = 20
# print(lst)


# try:
#     x = 1/0

# except ZeroDivisionError as e:
#     print("caught exception:", e)

# else:
#     print("no exceptions occurred.")

# finally:
#     print("always executed")

# class Example:
#     @staticmethod
#     def static_method():
#         return "static Method"

#     @classmethod
#     def class_method(cls):
#         return f"class method of {cls.__name__}"
    
# print(Example.static_method())
# print(Example.class_method())

# data = [1,2,3,4,5,6]

# it = iter(data)

# while True:
#     try:
#         print(next(it))

#     except Exception as e:
#         break

class faculty(): #class
    def __init__(self): #method
        self.id = int(input("Enter the id: "))
        self.name = input("enter name: ")
        self.salary = float(input("enter the salary: "))

    def display(self):
        print("faculty id", self.id)
        print("faculty name", self.name)
        print("faculty salary", self.salary)


a = faculty()
#a.putdata()
a.display()