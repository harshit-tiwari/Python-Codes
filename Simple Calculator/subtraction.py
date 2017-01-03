import calculate

def subtractFunc():
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
                    break
                except ValueError:
                    print("Please enter a number as your input")
            while True:
                try:
                    limit = int(input("How many numbers do you want to subtract from %s?: "%largerNumber))
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
            print("Wrong Choice for subtraction")
            break
