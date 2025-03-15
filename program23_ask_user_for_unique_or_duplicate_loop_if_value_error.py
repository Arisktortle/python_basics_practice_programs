#intialize a list for number inputs
entered_numbers = []

#create loop asking numbers for and checks if duplicate or unique
while True:
    try:
        # Ask user to input a number
        num = int(input("Enter a number (or type something non-numeric to exit): "))
        
        # Check if the number is unique or a duplicate
        if entered_numbers.count(num) == 0:
            print("Unique")
        else:
            print("Duplicate")
            
#add the inputted number in the list
        entered_numbers.append(num)

#terminate the program if invalid input
    except ValueError:
        print("Invalid input. Exiting the program.")
        break