#create a loop that prints 0 to 100 numbers
for num in range(101):
    if num % 10 != 0 and num %10 !=5: #checks if the number ends with 0 or 5
        print(num) #prints the number not ending in 0 or 5