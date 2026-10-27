# Decorators in python with arguments
def repeat(n):
    def my_func(func):
        def wrapper(name):
            for i in range(n):
                func(name)
        return wrapper
    return my_func

@repeat(3)
def greet(name):
    print(name)

def mul(a,b):
    def decorator(func):
        def wrapper():
            print(f"The multiplication of {a} and {b} is {a*b}")
            func()
        return wrapper
    return decorator

@mul(3,4)
def sum():
    a = 4
    b = 8
    print(f"The sum of {a} and {b} is {a+b}")


if __name__ == "__main__":
    greet("Suriya")

    sum()