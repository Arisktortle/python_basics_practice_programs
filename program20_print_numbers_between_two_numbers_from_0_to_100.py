#prompts to enter two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#loop that checks and print only the numbers in between
for num in range(num1, num2 + 1):
    print(num)