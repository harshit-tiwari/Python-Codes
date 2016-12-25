import calculate

print("This is a calculator. Enter your choices as asked below")
print("1 For Addition\n"
      "2 For Subtraction\n"
      "3 For Multiplication\n"
      "4 For Division")

choice = int(input("Enter your choice here : "))

if choice == 1:
    print("You have chosen to addition")
    operands = []
    number = int(input("How many numbers do you want to add? : "))
    for i in range(0, number):
        value = int(input("Enter the number %s here : "%(i+1)))
        operands.append(value)
    total = calculate.add(*operands)
    print("The sum of these numbers is : ", total)
elif choice == 2:
    print("You have chosen to Subtraction")
    largeNumber = int(input("Enter the larger number : "))
    smallNumber = int(input("Enter the smaller number : "))
    difference = calculate.subtract(smallNumber,largeNumber)
    print("The difference of the two numbers is ", difference)
elif choice == 3:
    print("You have chosen to Multiplication")
    operands = []
    number = int(input("How many numbers do you want to multiply? : "))
    for i in range(0, number):
        value = int(input("Enter the number %s here : " % (i + 1)))
        operands.append(value)
    product = calculate.multiply(*operands)
    print("The product of these numbers is : ", product)
elif choice == 4:
    dividend = int(input("Enter the dividend : "))
    divisor = int(input("Enter the divisor : "))
    division = calculate.divide(dividend,divisor)
    print("The division of the two numbers is ", division)
else:
    print("Wrong choice")