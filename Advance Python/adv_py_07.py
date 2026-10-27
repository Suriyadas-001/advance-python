# class and instance method
class Employee:
    company = "TCS"
    def __init__(self,name):
        self.name = name
    @classmethod
    def changeCompany(cls,newCompany): # Now here cls is not instance for an object 
        cls.company = newCompany # cls is a instance of the class
    
if __name__ == "__main__":
    e1 = Employee("Sujoy")
    e2 = Employee("Suriya")
    print(e1.name)
    print(e1.company)
    print("Before")
    print(e2.company)
    # Employee 2 switch company
    e2.company = "Cognigent"
    print("After")
    print(e2.company)

    # But actual value is not changed
    print(Employee.company)

    # here e2.company is created
    # we can create new var also
    e2.salary = 20000
    print(e2.salary)


    # Now if we want that is we change comapany it also change for Entire class then we need @classmethod

    e2.changeCompany("Wipro")
    print(Employee.company)
