#Function to act as a switch case for the selection that the user makes
def choice(selection):
    #Switch object to call the function related to the option selected
    #Lambda used so functions are only called when supposed to
    switch={
        "1": (DenToBin,"denary", "Converting number from Denary to Binary..."),
        "2": (BinToDen,"binary", "Converting number from Binary to Denary..."),
        "3": (DenToHex,"denary", "Converting number from Denary to Hexadecimal..."),
        "4": (HexToDen,"hexadecimal", "Converting number from Hexadecimal to Denary..."),
        "5": (BinToHex,"binary", "Converting number from Binary to Hexadecimal..."),
        "6": (HexToBin,"hexadecimal", "Converting number from Hexadecimal to Binary..."),
    }
    #Finding the option selected
    try:
        caseFunction, testType, casePrint = switch[selection]
        print(casePrint)
        number = input("Enter the number you want to convert : ").upper()
        if validInput(testType,number):
            return caseFunction(number)
    except : 
        print("Invalid Input Enterred")
        return True #Returning True incase invalid is accidental
        
#Function to check whether a number is valid, depending on what type it is supposed to be
#Function to ensure number input is valid for number type chosen
def validInput(choice,number):
    if choice == "hexadecimal":
        hex = {"0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"}
        for digit in number:
            if digit not in hex:
                print("Invalid Hexadecimal Number")
                return False
    elif choice == "binary":
        binary = {"0","1"}
        for digit in number:
            if digit not in binary:
                print("Invalid Binary Number")
                return False
    else:
        denary = {"0","1","2","3","4","5","6","7","8","9"}
        for digit in number:
            if digit not in denary:
                print("Invalid Denary Number")
                return False            
    return True
    
#Function to see whether the user wants to continue
def checkContinue():
    check = input("Would you like to continue? (Yes,No) : ").lower()
    if check == "yes":
        return True
    else:
        return False
    
#Function to convert Denary numbers to Binary
def DenToBin(number):
    number = int(number)
    #Finding the most significant binary number
    mostSignificant = 1
    index = 0
    while number >= mostSignificant*2:
        mostSignificant *=2
        index += 1
    #Finding the output binary number
    output = ""
    outputNumber = number #Creating a copy of the number variable to use later
    for i in range(index+1):
        if number - 2**index >= 0:
            output += "1"
            number -= 2**index
        else:
            output += "0"
        index -= 1
    print(str(outputNumber) + " in binary is : "  + output)

#Function to convert Binary numbers to Denary
def BinToDen(number):
    index = len(number)-1 #Setting up the pointer for the number
    total = 0
    #Looping through each number and multiplying by 2**index
    for digit in number :
        total += int(digit) * 2**index
        index -= 1
    print(number + " in Denary is : " + str(total))


#Function to convert Denary numbers to Hexadecimal
def DenToHex(number):
    number = int(number)
    #Finding most significant value
    mostSignificant = 1
    index = 0
    while number >= mostSignificant*16:
        mostSignificant *= 16
        index += 1
    #Finding out the output hexadecimal number
    output=""
    #Defining all of the hex values (That aren't integers)
    hexNumbers = {10:"A", 11:"B", 12:"C",13:"D",14:"E",15:"F"}
    #Looping through all of the indexes
    for i in range(index,-1,-1):
        #Skipping the index if a number has already been accounted for
        #Looping through all possible hex values
        for j in range(15,-1,-1):
            #Taking away the highest number possible
            if number - j*16**i >= 0:
                number -= j*16**i
                #Adding the number taken away to the string
                if j <10:
                    output += str(j)
                else:
                    output += hexNumbers.get(j)
                break
    print(output)    

#Function to convert Hexadecimal numbers to Denary
def HexToDen(number):
    hexValues = {"A" : 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15}
    index = len(number) - 1 #Setting up the pointer for the number
    total = 0
    #Looping through every digit
    for digit in number : 
        #Translating string to an int
        try : 
            digit = int(digit)
        except :
            digit = hexValues.get(digit)

        #Updating total and index
        total += digit * 16**index
        index -= 1
    print(number + " in Denary is " + str(total))

#Function to convert Binary numbers to Hexadecimal
def BinToHex(number):
    #Making the number a group of 4
    while len(number) % 4 != 0:
        number = "0" + number
    #Making an array of the different sublists
    binSublist = []
    for i in range(0,len(number),4):
        binSublist.append(number[i:i+4])
    #Working out the output for this number
    output=""
    #Working out the value of each sublist
    #Looping through each sublist
    for subList in binSublist:
        subValue = 0
        #Looping through each index and item in the sublists
        for i,item in enumerate(subList):
            #Working out the subLists value
            #len(subList)-1-i is used to loop through the subList indexes backwards
            subValue += int(item) * 2**(len(subList)-1-i)
        #Working out the hex value of the subvalue
        if subValue < 10:
            output += str(subValue)
        else:
            hexValues = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
            output += hexValues.get(subValue)
    print(number + " in Hexadecimal is " + output)

#Function to convert Hexadecimal numbers to Binary
def HexToBin(number):
    #Function implemented to remove 0s from the front of the Hex Numbers
    def stripZeros(string):
        for char in string:
            if char == "1":
                break
            string = string[1:]
        return string

    #Main Function Code
    #Defining the conversions from a hex number to a binary number
    hexConversion = {"0":"0000", "1":"0001", "2":"0010", "3":"0011", 
                    "4":"0100", "5":"0101", "6":"0110", "7":"0111", 
                    "8":"1000", "9":"1001", "A":"1010", "B":"1011", 
                    "C":"1100", "D":"1101", "E":"1110", "F":"1111"}
    #Working out the output
    output = ""
    for char in number : 
        output += hexConversion.get(char)
    #Stripping the 0s from the front of the binary number
    output = stripZeros(output)
    print(number + " in Binary is " + output)

#The if statement below is used to ensure that this code is only run if this file is run as a script
#If this isn't implemented, this code will be run every time something from this function is imported
#Ie, the GUI file will run this code if the if statement wasn't in place
if "__main__" == __name__:
    def main():
        check = True
        #Allowing the user to be able to do this multiple times
        while check == True:
            #Getting the input from the user
            print()
            print("Please select the option that you would like to convert : ")
            print("1. Denary to Binary")
            print("2. Binary to Denary")
            print("3. Denary to Hexadecimal")
            print("4. Hexadecimal to Denary")
            print("5. Binary to Hexadecimal")
            print("6. Hexadecimal to Binary")
            print("Enter Quit to Leave")
            print()
            selection = input("Please select your input : ").lower()
            print()

            #Checking to see if the user wants to leave
            if selection == "quit":
                break

            #Calling the function related to the option selected
            choice(selection)
            check = checkContinue()
    main()