# # pythonic approach 
# class Person:
#     def __init__(self,name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self,name):
#         self._name = name

#     @name.deleter
#     def name(self):
#         del self._name


# p = Person("Sujoy")

# p._name = "Suriya"
# print(p.name)
# # del p.name
# # print(p.name)



# Getters and setters in python (traditional approach)
import time
class IndianBank:
    def __init__(self,name,account,amount):
        self._name = name
        self._account = account
        self._amount = amount

    @property
    def money(self): # getter
        print(f"Your current Balance is {self._amount}")

    @money.setter
    def money(self,money): # setter
        self._amount += money
        print(f"Your A/c {self._account} is credited with Rs.{money:.2f} Available balance is {self._amount:.2f} on {time.ctime()}")

if __name__ == "__main__":
    S_Das = IndianBank("Sujoy Das",3578,100)

    S_Das.money = 12000
    S_Das.money