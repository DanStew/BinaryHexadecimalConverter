def main():
    #Function to act as a switch case for the selection that the user makes
    def choice(selection):
        #Switch object to call the function related to the option selected
        #Lambda used so functions are only called when supposed to
        switch={
            "1": DenToBin,
            "2": BinToDen,
            "3": DenToHex,
            "4": HexToDen,
            "5": BinToHex,
            "6": HexToBin,
        }
        #Finding the option selected
        try:
            return switch[selection]() #Allowing the user to quit at this stage, after number converted
        except : 
            print("Invalid Input Enterred")
            return True #Returning True incase invalid is accidental
        
    #Function to check whether a number is valid, depending on what type it is supposed to be
    #Function to ensure number input is valid for number type chosen
    def validInput(choice,number):
        if choice == "hex":
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
    def DenToBin():
        print("Converting number from Denary to Binary")
        number = input("Enter the number you want to convert : ")
        if validInput("denary",number):
            print("Valid Denary Number")
        return checkContinue()

    #Function to convert Binary numbers to Denary
    def BinToDen():
        print("Converting number from Binary to Denary")
        number = input("Enter the number you want to convert : ")
        if validInput("binary",number):
            index = len(number)-1 #Setting up the pointer for the number
            total = 0
            #Looping through each number and multiplying by 2**index
            for digit in number :
                total += int(digit) * 2**index
                index -= 1
            print(number + " in Denary is : " + str(total))
        return checkContinue()

    #Function to convert Denary numbers to Hexadecimal
    def DenToHex():
        print("Converting number from Denary to Hexadecimal")
        return checkContinue()

    #Function to convert Hexadecimal numbers to Denary
    def HexToDen():
        print("Converting number from Hexadecimal to Denary")
        number = input("Enter the number you want to convert : ").upper()
        if validInput("hex",number):
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
        return checkContinue()

    #Function to convert Binary numbers to Hexadecimal
    def BinToHex():
        print("Converting number from Binary to Hexadecimal")
        return checkContinue()

    #Function to convert Hexadecimal numbers to Binary
    def HexToBin():
        print("Converting number from Hexadecimal to Binary")
        return checkContinue()

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
        check = choice(selection)

main()

