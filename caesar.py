while True:
    state = input("Would you like to (g)enerate or (s)olve? Or do you need (h)elp?\n")
    if state in ['g', 's']:
        break
    elif state == 'h':
        print("This program is a Caesar cipher generator or solver")
        print("Entering 'g' at this point will allow you to create a Caesar cipher encoded message of any string of "
              "letters you enter")
        print("Entering 's' will solve an already encoded message that you enter")
        print("Later, you will be prompted to choose a magnitude, this will determine how many places along"
              "the alphabet each letter in the string will be shifted\n")
    elif state == 'c':
        print("A quick and complete one day project created by unemployed CS grad Oisín Whelan")
    else:
        print("Please enter either 'g' or 's' and press Enter.\n")

while True:
    string = input("Enter your string:\n")
    if not string:
        print("Please enter a string.\n")
        continue
    check = string.replace(" ", "a")
    if check.isalpha():
        break
    else:
        print("Please only enter English alphabet letters.\n")

while True:
    num = input("Enter the cipher's magnitude:\n")
    if not num.isnumeric():
        print("Please enter an integer.\n")
    else:
        break
mag = int(num) % 26
if state == 's':
    mag *= -1

outstring = []
words = string.split()

for word in words:
    output = ""
    for c in word:
        ascii = ord(c)
        ascii += mag
        if ascii > 122 or (ascii > 90 and ord(c) < 90):
            ascii -= 26
        elif (ascii < 97 and ord(c) > 97) or ascii < 65:
            ascii += 26
        c = chr(ascii)
        output += c
    outstring.append(output)

s = " "
print("Your coded message is: " + s.join(outstring))
