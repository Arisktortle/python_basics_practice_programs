#prompt the user to input 10 numbers
nums = [int(input(f"Enter number {i+1}: ")) for i in range(10)]

#check for duplicates, print only the first entry
for i in range(10):
    if nums.count(nums[i]) == 1 or nums.index(nums[i]) == i: 
        print(nums[i]) #print numbers, those with dupes only first entry