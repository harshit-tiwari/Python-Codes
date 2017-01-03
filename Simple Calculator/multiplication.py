import calculate

def multiplyFunc():
    print("You have chosen to Multiplication")
    operands = []
    while True:
        try:
            number = int(input("How many numbers do you want to multiply? : "))
            break
        except ValueError:
            print("Please enter a number as your input")
    for i in range(0, number):
        while True:
            try:
                value = int(input("Enter the number %s here : " % (i + 1)))
                break
            except ValueError:
                print("Please enter a number as your input")
        operands.append(value)
    product = calculate.multiply(*operands)
    print("The product of these numbers is : ", product)
