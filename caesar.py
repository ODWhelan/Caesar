# Determine if generating or solving
while True:
    state = input("Would you like to (g)enerate or (s)olve? Or do you need (h)elp?\n")
    if state in ['g', 's']:
        break
    elif state == 'h':
        print("This program is a Caesar cipher generator or solver.")
        print("Entering 'g' at this point will allow you to create a Caesar cipher encoded message of any string of "
              "letters you enter.")
        print("Entering 's' will solve an already encoded message that you enter.")
        print("Later, you will be prompted to choose a magnitude, this will determine how many places along"
              "the alphabet each letter in the string will be shifted.\n")
    elif state == 'c':
        print("A quick and complete two hour project created by unemployed CS grad Oisín Whelan")
    else:
        print("Please enter either 'g' or 's' and press Enter.\n")

# Input string
while True:
    string = input("Enter your string:\n")
    if not string:
        print("Please enter a string.\n")
        continue
    check = string.replace(" ", "")
    if not check:
        print("Please enter at least one letter.")
    elif check.isalpha():
        break
    else:
        print("Please only enter English alphabet letters and spaces.\n")

# Shifting number
while True:
    num = input("Enter the cipher's magnitude:\n")
    if not num.isnumeric():
        print("Please enter an integer.\n")
    else:
        break

# Convert number to int, note that shifting by greater than 26 is equivalent to it mod 26
mag = int(num) % 26
# Solving is also equivalent to generating but the other way
if state == 's':
    mag *= -1

# Setting up the final output and splitting the string into words
outstring = []
words = string.split()

for word in words:
    output = ""
    for c in word:
        ascii = ord(c)
        ascii += mag
        # Positive value wraparounds, first for lower case then for upper case
        if ascii > 122 or (ascii > 90 and ord(c) < 90):
            ascii -= 26
        # Negative value wraparounds, as above
        elif (ascii < 97 and ord(c) > 97) or ascii < 65:
            ascii += 26
        c = chr(ascii)
        output += c
    outstring.append(output)

s = " "
print("Your coded message is: " + s.join(outstring))
