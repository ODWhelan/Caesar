state = input("Would you like to (g)enerate or (s)olve?\n")
while True:
    string = input("Enter your string:\n")
    if not string:
        print("Please enter a string.\n")
    elif string.isalpha():
        break
    else:
        print("Please only enter English alphabet letters.\n")
num = int(input("Enter the cipher's magnitude:\n"))
num = num % 26
if state == 's':
    num *= -1

output = ""

for c in string:
    ascii = ord(c)
    ascii += num
    if ascii > 122 or (ascii > 90 and ord(c) < 90):
        ascii -= 26
    elif (ascii < 97 and ord(c) > 97) or ascii < 65:
        ascii += 26
    c = chr(ascii)
    output += c

print("Your coded message is: " + output)
