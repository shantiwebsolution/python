num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"(Method:loop)The factorial of {num} is {factorial}")

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)   


print(f"(Method:recursion)The factorial of {num} is {factorial_recursive(num)}")    