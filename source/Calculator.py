try:
    from time import *
    from datetime import *
    from calc_operations import *
    print("Initializing Calculator")
    sleep(1)
    print("Importing database from Programmer24680")
    sleep(2)
    print("Database imported successfully")
    sleep(0.75)
    print("Now Launching.")
    sleep(0.5)
    print(f"Date and Time: {datetime.now()}")
    sleep(0.25)



    while True:

        try:
            num1 = float(input("Enter the first number: "))
            sleep(0.25)
            num2 = float(input("Enter the second number: "))
            sleep(0.25)
            storage = Calculator(num1, num2)
        except ValueError:
            sleep(0.25)
            print("You have to enter numbers only")
            sleep(0.75)
            break

        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")


        choice = input("Enter your choice (1/2/3/4) : ")

        if choice in ("1", "2", "3", "4"):
            if choice == "1":
                print(f"Result is: {storage.add()}")
            elif choice == "2":
                print(storage.sub())
            elif choice == "3":
                print(storage.mult())
            else:
                print(storage.div())
        else:
            print("You can enter choice in (1/2/3/4) only.")
            sleep(0.5)
            break

    print("Now Exiting...")

except EOFError:
    print("\n\n^C Keyboard interrupt. Exiting")
