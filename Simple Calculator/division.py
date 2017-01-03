import calculate
import MyExceptions
def divideFunc():
    print("You have chosen Division")
    while True:
        try:
            dividend = int(input("Enter the dividend : "))
            break
        except ValueError:
            print("Please enter a number as your input")
    while True:
        try:
            divisor = int(input("Enter the divisor : "))
            if divisor == 0:
                raise DivisorZero
            break
        except ValueError:
            print("Please enter a number as your input")
        except DivisorZero:
            print("The divisor cannot be zero, please enter again.")
    
    division = calculate.divide(dividend,divisor)
    print("The division of the two numbers is ", division)

        
