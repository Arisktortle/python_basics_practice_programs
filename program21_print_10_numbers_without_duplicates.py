#input 10 numbers
nums = [int(input(f"Enter number {a+1}: ")) for a in range(10)]

#loop that checks and display numbers that don't have duplicate
for num in nums:
    if nums.count(num) == 1:
        print(num) #print the numbers