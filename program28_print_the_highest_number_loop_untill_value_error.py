#create a variable for highest number
highest_number = None

#create loop that input numbers 
while True:
    user_input = input("Please enter a number: ")

    #checks if the input is valid
    if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
        number = int(user_input)
        
#intialize in the count and store in the variable if highest number

#terminate the program if invalid input
    else:

        print("Invalid input! Exiting...")
        break
    
#print the highest number input