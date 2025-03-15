#create a dictionary to store number inputs
number_count = {}

#input 10 numbers
while True:
    user_input = input("Please enter a number: ")

    #check if valid
    if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
        number = int(user_input)
        
#count for the number times the number is inputted
        if number in number_count:
            number_count[number] += 1
        else:
            number_count[number] = 1

#if an input is invalid exit program
    else:
        print("Invalid input! Exiting...")
        break
    
#check the number with the most duplicates
#print that number