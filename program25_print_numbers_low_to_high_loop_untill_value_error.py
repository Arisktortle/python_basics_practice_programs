#create a list for number inputs
numbers = []

#input numbers and loop until value error
while True:
    user_input = input("Please enter a number: ")

    #check if valid input, then add to the list
    if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()): 
        number = int(user_input)
        numbers.append(number) 
    else:
        #if invalid input break the loop
        print("Invalid input! Exiting...")
        break
    
#arrange the list in ascending order
numbers.sort()

#print the list from lowest to highest