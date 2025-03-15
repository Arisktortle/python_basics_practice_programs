#create list for number input
numbers = []

#input 10 numbers with loop
for i in range(10):
    number = int(input(f"Please enter number {i+1}: "))
    numbers.append(number)
    
#create dictionary to check number count for checking dupes
number_count = {}

#check and count for duplicates of input numbers
for num in numbers:
    if num in number_count:
        number_count[num] += 1
    else:
        number_count[num] = 1
        
duplicate = [num for num, count in number_count.items() if count > 1]

#print numbers with dupes
if duplicate:
    print("List of numbers with dupes:", duplicate)
else:
    print("No duplicates found.")