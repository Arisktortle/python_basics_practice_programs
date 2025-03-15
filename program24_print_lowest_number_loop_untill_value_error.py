#create a variable to store a lowest number input
lowest_number = None

#create loop that input numbers
while True:
    user_input = input("Please enter a number: ")

    try:
        number = int(user_input)
        
        #if valid input, and lowest number, set the value for lowest_number
        if lowest_number is None or number < lowest_number:
            lowest_number = number

    #check for invalid input
    except ValueError:
        print("Invalid input! Exiting...") #if invalid input break loop
        break
    
#print the numbers entered after loop terminate