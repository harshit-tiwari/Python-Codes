import calculate

flag = True
while flag:
    print("This is a calculator. Enter your choices as asked below")

    print("1 For Addition\n"
          "2 For Subtraction\n"
          "3 For Multiplication\n"
          "4 For Division")
    choice = 0
    number = 0
    value = 0
    subtractChoice = 0
    largeNumber = 0
    smallNumber = 0
    largerNumber = 0
    limit = 0
    dividend = 0
    divisor = 0
    wrongChoice = False
    while True:
        try:
            choice = int(input("Enter your choice here : "))
        except ValueError:
            print("Please enter a number as your choice")

        if choice == 1:
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
            break

        elif choice == 2:
            while True:
                print("You have chosen Subtraction")
                print("Enter your choice as below \n"
                     "1  for Two numbers' processing \n"
                    "2  for more than two numbers' processing")
                while True:
                    try:
                        subtractChoice = int(input("Enter your choice : "))
                        break
                    except ValueError:
                        print("Please enter a number as your input")

                if subtractChoice == 1:
                    while True:
                        try:
                            largeNumber = int(input("Enter the larger number : "))
                            break
                        except ValueError:
                            print("Please enter a number as your input")
                    while True:
                        try:
                            smallNumber = int(input("Enter the smaller number : "))
                            break
                        except ValueError:
                            print("Please enter a number as your input")
                    difference = calculate.subtract(smallNumber,largeNumber)
                    print("The difference of the two numbers is ", difference)
                    break
                elif subtractChoice == 2:
                    while True:
                        try:
                            largerNumber = int(input("Enter the largest number from which you want to subtract other numbers : "))
                        except ValueError:
                            print("Please enter a number as your input")
                    while True:
                        try:
                            limit = int(input("How many numbers do you want to subtract from %s? "%largerNumber))
                            break
                        except ValueError:
                            print("Please enter a number as your input")
                    smallerNumber = []
                    for i in range(0, limit):
                        while True:
                            try:
                                value = int(input("Enter the number %s here : "%(i+1)))
                                break
                            except ValueError:
                                print("Please enter a number as your input")
                        smallerNumber.append(value)
                    totalSmallerNumber = 0
                    for i in smallerNumber:
                        totalSmallerNumber += i
                    difference = calculate.subtract(totalSmallerNumber, largerNumber)
                    print("The difference of the numbers is ", difference)
                    break
                else:
                    print("Wrong Choice")
                    break

        elif choice == 3:
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

        elif choice == 4:
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
                    break
                except ValueError:
                    print("Please enter a number as your input")
            division = calculate.divide(dividend,divisor)
            print("The division of the two numbers is ", division)

        else:
            print("This is not a valid choice. Please Enter your choice again.")

    innerFlag = True
    while innerFlag:
        contChoice = input("Do you want to continue?(Y/N) : ")
        if contChoice == 'Y' or contChoice == 'y':
            flag = True
            innerFlag = False
        elif contChoice == 'N' or contChoice == 'n':
            print("Bye!!")
            flag = False
            innerFlag = False
        else:
            print("Wrong Choice. Please enter the choice again.")
            innerFlag = True










