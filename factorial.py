

def fact(num):
    if num < 0:
        print("Factorial is not defined for negative numbers")
        exit
    result=1
    for i in range(1,num+1):
        result=result*i
    return result


num=int(input("Enter a number : "))
# print(fact(num))

print(f"factorial of {num} is {fact(num)}")