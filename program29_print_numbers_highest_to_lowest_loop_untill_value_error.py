#create a list to store number inputs
numbers = []

#create a loop that input numbers
while True:
    user_input = input("Please enter a number: ")
    
    
    if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()): #check the input for value error
        number = int(user_input)
        numbers.append(number)  #places the input into the numbers list
        
    else:
        #if value error terminate the loop
        print("Invalid input! Exiting...")
        break
    
#arrange the inputs highest to lowest
#print the inputs in descending order