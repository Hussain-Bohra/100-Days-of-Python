# Write a program to print factorial using recursion.
def myfactorial(num):

    if(num < 2):
        return 1

    else:
        return (num * myfactorial(num - 1))


# num = int(input("Enter a Number: "))
# print(f"\nFactorial of {num} is: {myfactorial(num)}")



# Write a program to print fibonacci series using recursion.
def myfibonacci(num):
    if(num == 0):
        return 0
        
    elif(num == 1):
        return 1

    else:
        return myfibonacci(num - 1) + myfibonacci(num - 2)
    


num = int(input("Enter a Number: "))
print(f"\nFibonacci Series of {num} is: {myfibonacci(num)}") 

