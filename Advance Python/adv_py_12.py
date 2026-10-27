# walrus operator (:=)
if __name__ == "__main__":
    # data = input("Enter a value (quit or exit) :: ")
    # while data != "quit":
    #     print(data)
    #     data = input("Enter a value (quit or exit) ::")

    # while (data := input("Enter a value (quit or exit) ::")) != "quit":
    #     print(data)
    # while (data = input("Enter a value (quit or exit) :: ")) != "quit":
    #     print(data) # It show an error
    numbers = [1,2,3,4,5]
    x = [i for i in numbers]
    print(x)
    # without walrus
    num1 = [x**2 for x in numbers if x**2>10]
    print(num1)

    # with walrus
    num2 = [y for x in numbers if (y:=x**2)>10]
    print(num2)