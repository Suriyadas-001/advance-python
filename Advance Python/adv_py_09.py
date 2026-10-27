# access modifier

class IndianBank:
    def __init__(self,name):
        self.__name = name
    @property # getter
    def name(self):
        return self.__name

    @name.setter
    def name(self,newName):
        self.__name = newName


if __name__ == "__main__":
    c1 = IndianBank("Ajay")
    # print(f"1st customer is {c1.__name}") # It is private attribute so it show an error But there is no private and protected in python

    # We can access the name without getter
    # How ?

    print(f"The name is {c1._IndianBank__name}")

    # Using getter
    print(f"The name is {c1.name}")

    # change the name
    c1.name = "Bijay"
    print(f"The new name is {c1.name}")

