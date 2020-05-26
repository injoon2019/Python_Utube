class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("division calculator")
    num1= int(input("first num"))
    num2 = int(input("second num"))
    if num1 >=10 or num2 >=10:
        raise BigNumberError
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("Wrong val")
except BigNumberError:
    print("Only one digit number")
