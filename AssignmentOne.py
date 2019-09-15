
print("Please Select From the Following Options")
print("Press 1 For Addition")
print("Press 2 For Subtraction")
print("Press 3 For multiplication")
print("Press 4 For Division")
print("Press 5 For Checking Equal or Not")
print("Press 6 For Checking Greater than or not")
print("Press 7 For Checking Smaller than or not")
print("Press 8 For Checking odd or Even")
print("Press 9 For Quiting The Game")


def math():

    # game stops only when the user wants
    while True:
        # input section
        MenuSelection = int(input("\nSelect From the above:"))


        # doing the math

        if MenuSelection == 1 :
            First_number = int(input("Enter First Number:"))
            Second_number = int(input("Enter Second Number"))
            print("The Result is", First_number + Second_number)

        elif MenuSelection == 2 :
            First_number = int(input("Enter First Number:"))
            Second_number = int(input("Enter Second Number"))
            print("The Result is", First_number - Second_number)

        elif MenuSelection == 3 :
            First_number = int(input("Enter First Number:"))
            Second_number = int(input("Enter Second Number"))
            print("The Result is", First_number * Second_number)

        elif MenuSelection == 4 :
            First_number = int(input("Enter First Number:"))
            Second_number = int(input("Enter Second Number"))
            print("The Result is", First_number / Second_number)

        elif MenuSelection == 5 :
            First_number = int(input("Enter First Number:"))
            Second_number = int(input("Enter Second Number"))
            if First_number == Second_number :
                print("They are Equal")
            else:
                print("They are Different")

        elif MenuSelection == 6:
            First_number = int(input("Enter First Number:"))
            Second_number = int(input("Enter Second Number"))
            if First_number > Second_number:
                print(First_number,"Is bigger")
            elif Second_number > First_number :
                print(Second_number,"Is bigger")

        elif MenuSelection == 7:
            First_number = int(input("Enter First Number:"))
            Second_number = int(input("Enter Second Number"))
            if First_number < Second_number:
                print(First_number,"Is Smaller")
            elif Second_number < First_number :
                print(Second_number,"Is Smaller")

        elif MenuSelection == 8:
            First_number = int(input("Enter First Number:"))
            Second_number = int(input("Enter Second Number"))
            if (First_number % 2) == 0 and (Second_number % 2) == 0:
                print("Both Are Even")

            elif (First_number % 2) != 0 and (Second_number % 2) == 0:
                print(First_number,"Is Odd ")

            elif (First_number % 2) == 0 and (Second_number % 2) != 0:
                print(Second_number,"Is Odd")
            elif (First_number % 2) != 0 and (Second_number % 2) != 0:
                print("Both Are odd")
        elif MenuSelection == 9:
            print("Bye Bye......")
            exit()
        else:
            print("Incorrect Selection")
            math()

math()