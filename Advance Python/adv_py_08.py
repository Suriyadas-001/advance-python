# static method
class ArithmaticOp:
    def sum(self,a,b):
        return a+b
    @staticmethod
    def mul(a,b):
        return a*b

if __name__ == "__main__":
    ao = ArithmaticOp()
    print(f"Sum {ao.sum(2,7)}")
    print(f"Mul {ao.mul(2,7)}")
    print(f"Mul {ArithmaticOp.mul(2,7)}")
    # print(f"Mul {mul(2,7)}") # It show an error
