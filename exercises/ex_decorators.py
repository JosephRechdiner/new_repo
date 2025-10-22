# 1
def decorator(func):
    def wrapper():
        print("Start function")
        func()
        print("End function")
    return wrapper

@decorator
def prints_hello():
    print("hello")

# prints_hello()


# 2
import time
def time_to_print_decorator(func):
    def wrapper():
        start = time.time()
        func()
        print(time.time() - start)
    return wrapper

@time_to_print_decorator
def prints_hi():
    print("hi")

# prints_hi()


# 3
def prints_items_decorator(func):
    def wrapper(*args):
        for item in args:
            print(item)
        print(func(args))
    return wrapper

@prints_items_decorator
def count_items(items):
    return len(items)

# count_items(1,2,3)


# 4
def uppercase_decorator(func):
    def wrapper():
        s = func()
        return s.upper()
    return wrapper

@uppercase_decorator
def returns_string():
    return "string"

# print(returns_string())


# 5
count = 0
def count_calls(func):
    def wrapper():
        func()
        global count
        count += 1
        print(count)
    return wrapper

@count_calls
def prints_hi():
    print("hi")

# prints_hi()
# prints_hi()


# 6
def authentication_check_decorate(func):
    def wrapper(name, is_admin):
        if is_admin: 
            func(name, is_admin)
        else:
            print(f"{name} is not admin")
    return wrapper

@authentication_check_decorate
def print_hi(name, is_admin):
    print(f"hi {name} you are admin")

# print_hi("yossi", True)

# 7
def memoization_decorator(func):
    cach = {}
    def wrapper(*args):
        if args not in cach:
            cach[args] = func(*args)
        return cach[args]
    return wrapper

@memoization_decorator
def calc_add(*args):
    return sum(args)

# print(calc_add(1,2,3))
# print(calc_add(1,2,3))
# print(calc_add(1,2,4))
# print(calc_add(1,2,3))

# 8
def retry_decorator(func):
    def wrapper():
        for i in range(3):  
            try:  
                func()
            except ZeroDivisionError:
                print("tried")
    return wrapper  
    
@retry_decorator
def devition():
    return 4 / 0

# devition()

# 9
def decorator_with_parameter(func):
    def wrapper(num):
        for _ in range(num):
            func(num)
    return wrapper

@decorator_with_parameter
def print_hi(num):
    print("hi")


# print_hi(5)

# 10
