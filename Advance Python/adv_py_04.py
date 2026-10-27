# chaing multiple decorator
def uppercase(func):
    def wrapper(name):
        return func(name).upper()
    return wrapper

def excalim(func):
    def wrapper(name):
        return func(name) + "!!!"
    return wrapper

def Hello(func):
    def wrapper(name):
        return "Hello, " + func(name)
    return wrapper

@Hello
@uppercase
@excalim
def greet(name):
    return name

if __name__ == "__main__":
    print(greet("Suriya"))