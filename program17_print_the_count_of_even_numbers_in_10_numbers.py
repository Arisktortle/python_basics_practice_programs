#input 10 numbers
even = 0
for a in range(10):
    num = int(input(f"Enter number {a+1}: "))
    
#check and count the even numbers
    if num % 2 == 0:
        even += 1
        
#print the count
print("The number of even numbers is:", even)