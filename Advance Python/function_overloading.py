# function overloading

# this is not correct approach in python function overloading


# def my_func():
#     print("Hello Sir")
# def my_func(name):
#     print(f"Hello {name}")

def my_func(name=None):
    if name is None:
        print("Hello Sir")
        return
    print(f"Hello {name}")


# def my_func(name="Sir"):
#     print(f"Hello {name}")

if __name__ == "__main__":
    my_func()