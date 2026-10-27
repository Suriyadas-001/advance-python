# Decorators 1
def my_dec1(func):
    def wrapper():
        print("Before function calling")
        func()
        print("After function calling")
    return wrapper


def my_dec2(func):
    def wrapper(name):
        print("Before function calling")
        func(name)
        print("After function calling")
    return wrapper

@my_dec1
def greet1():
    print("Hello, Sir!!!")

@my_dec2
def greet2(name):
    print(f"Hello, {name}!!!")

if __name__ == "__main__":
    greet1()

    print("After function overloading")
    greet2("Suriya")