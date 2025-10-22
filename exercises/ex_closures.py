# 1
def power_of(n):
    def power(base):
        return base ** n
    return power

x = power_of(2)
# print(x(3))

# 2
count = 0
def outer():
    def inner():
        global count
        count += 1    
    inner()
    return count

x = outer()
y = outer()
z = outer()

# print(z)

# 1
x = 10
def show():
    global x
    x -= 5

show()
# print("Inside:", x)
# print("Outside:", x)

# 2
count = 0
def add():
    global count
    count += 1

add()
# print(count)

# 3
msg = "hi"
def outer():
    msg = "Hello"
    def inner():
        print(msg)
    inner()
# outer()

# 4
def counter():
    num = 0
    def add_one():
        nonlocal num
        num += 1
        print(num)
    add_one()
# counter()

# 5
name = "Tom"
def greet():
    global name
    name = "Ben"
    print("Hi", name)
# greet()
# print("Bye", name)

# 6
def make_greeter(name):
    def greet():
        print("Hi", name)
    return greet
say_hi = make_greeter("Dudu")
# say_hi()

# 7
def discount_factory(percent):
    def apply(price):
        return price - (price * percent / 100)
    return apply
student = discount_factory(10)
vip = discount_factory(25)
# print(vip(100))

# 8
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

# double = make_multiplier(2)
# triple = make_multiplier(3)

# print(double(2))
# print(triple(2))

total_score = 0
def player(name):
    score = 0
    def add_points(points):
        nonlocal score
        score += points
        global total_score
        total_score += points
        print(f"{name}: {score} points (Total: {total_score})")
    return add_points

score = 0

# alice = player("Alice")
# bob = player("Bob")        
# alice(10)
# bob(20)
# alice(15)
# bob(35)

# def my_decorator(func):
#     def wrapper():
#         print("decorator action")
#         func()
#     return wrapper


# @my_decorator
# def print_hello():
#     print("hello")


# print_hello()

