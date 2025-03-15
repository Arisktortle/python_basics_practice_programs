#create list for number input
numbers = []

#input 10 numbers with loop
for i in range(10):
    number = int(input(f"Please enter number {i+1}: "))
    numbers.append(number)
    
#create dictionary to check number count for checking dupes
number_count = {}

#check for duplicates of input numbers
#print numbers with dupes