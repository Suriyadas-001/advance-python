# Exception Handling
def divide(a,b):
    return a/b


class CustomError(Exception):
    def __init__(self,message = "Age must be 18 or Older"):
        self.message =  message
        super.__init__(self.message)

def verify_age(age):
    if age<18:
        raise CustomError()
    elif age<0 or age>110:
        raise CustomError("Invalid age")

if __name__ == "__main__":
    # In-built Exceptions
    # try:
    #     print(divide(3,6))
    # except Exception as e:
    #     print(e)
    # finally:
    #     print("Our code is ok")
    try:
        verify_age(6)
        print("Welcome")
    except Exception as e:
        print(e)
    finally:
        print("Done")