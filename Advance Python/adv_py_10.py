# *args and **kwargs

# 1. *args - It take all attribute as a tuple
# Exaple - 1
def Ex_args_1(*args):
    for val in args:
        print(val)
# Exaple - 2
def Ex_args_2(*Suriya): # Here '*' is important not argument name
    print("Hello Sir")


# 2. **kwargs
# Example - 1
def Ex_kwargs_1(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

def Ex_kwargs_2(**Sujoy):
    print("Hello Sir!!!")

if __name__ == "__main__":
    # Ex_args_1(1,3,5,65)
    # Ex_args_2()

    
    Ex_kwargs_1(a = 1,b = 2)
    Ex_kwargs_2()
