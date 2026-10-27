# Decorators 2

def my_func(func):
    def my_ch(name="Boss"):
        print("Before")
        func(name)
        # print("After")
    return my_ch

@my_func
def greet(name):
    print(f"Hello, {name}!!!")


if __name__ == "__main__":
    greet("Suriya")