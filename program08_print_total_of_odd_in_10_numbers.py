#input 10 numbers
odd = 0
for i in range(10):
    number = int(input(f"Please enter number {i+1}: "))
    
#check if odd number and count the number of odds
    if number % 2 != 0:
       odd += 1
    
#print total of odd counted
print("Total number of odd numbers:", odd)