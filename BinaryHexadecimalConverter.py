
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
    
    #Function to convert Denary numbers to Binary
    def DenToBin():
        print("Converting number from Denary to Binary")
        return True

    #Function to convert Binary numbers to Denary
    def BinToDen():
        print("Converting number from Binary to Denary")
        return True

    #Function to convert Denary numbers to Hexadecimal
    def DenToHex():
        print("Converting number from Denary to Hexadecimal")
        return True

    #Function to convert Hexadecimal numbers to Denary
    def HexToDen():
        print("Converting number from Hexadecimal to Denary")
        return True

    #Function to convert Binary numbers to Hexadecimal
    def BinToHex():
        print("Converting number from Binary to Hexadecimal")
        return True

    #Function to convert Hexadecimal numbers to Binary
    def HexToBin():
        print("Converting number from Hexadecimal to Binary")
        return True

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

        #Checking to see if the user wants to leave
        if selection == "quit":
            break

        #Calling the function related to the option selected
        check = choice(selection)
        print(check)

main()

