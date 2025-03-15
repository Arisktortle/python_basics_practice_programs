#create a list for number input
numbers = []

#loop that ask to input numbers
while True:
    try:
        num = int(input("Enter a number (or type something non-numeric to exit): "))
        
#adds the inputted number into the list
        numbers.append(num)

#check for value error, terminate if yes
    except ValueError:
        print("Invalid input. Exiting the program.")
        break
    
#sort the number inputted in decreasing
#print the inputted numbers from the list