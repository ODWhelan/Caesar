state = input("Would you like to (g)enerate or (s)olve?\n")
while True:
    string = input("Enter your string:\n")
    if not string:
        print("Please enter a string.\n")
    elif string.isalpha():
        break
    else:
        print("Please only enter English alphabet letters.\n")
num = input("Enter the cipher's magnitude:\n")

