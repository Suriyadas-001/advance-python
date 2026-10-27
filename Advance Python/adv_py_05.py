# Getters and setters in python (traditional approach)
import time
class IndianBank:
    def __init__(self,name,account,amount):
        self._name = name
        self._account = account
        self._amount = amount
    # setter
    def credit(self,money):
        self._amount += money
        print(f"Your A/c {self._account} is credited with Rs.{money:.2f} Available balance is {self._amount:.2f} on {time.ctime()}")
    # getter
    def debit(self,money):
        self._amount -= money
        print(f"Your A/c {self._account} is debited Rs.{money:.2f} Available balance is {self._amount:.2f} on {time.ctime()}")

if __name__ == "__main__":
    S_Das = IndianBank("Sujoy Das",3578,100)

    S_Das.credit(12000)
    time.sleep(10)
    S_Das.debit(10000)