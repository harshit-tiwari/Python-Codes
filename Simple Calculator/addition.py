import calculate

def addFunc():
    print("You have chosen Addition")
    operands = []
    number = 0
    while True:
        try:
            number = int(input("How many numbers do you want to add? : "))
            break
        except ValueError:
            print("Please enter a number as your input")

    for i in range(0, number):
        while True:
            try:
                value = int(input("Enter the number %s here : "%(i+1)))
                break
            except ValueError:
                print("Please enter a number as your input")
        operands.append(value)
    total = calculate.add(*operands)
    print("The sum of these numbers is : ", total)
    
