#create value for sum and total count of numbers
sum = 0
numbers_count = 0

#create loop that asks user for numbers untill value error
while True:
    user_input = input("Please enter a number: ")

    if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()): #checks if the input is valid
        number = int(user_input)
        total_sum += number  
        count += 1  #count the total number
        
    else:
        print("Invalid input! Exiting...") #if the input is valid break the loop
        break
    
#calculate the average by getting the sum of all divided by the total count
#print the result