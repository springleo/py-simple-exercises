
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1): # Check divisors up to square root of the number
        if n%i==0: # If divisible, it's not a prime number
            return False
    return True

num=int(input("Enter any number : "))

result=is_prime(num)

if result:
    print(f"{num} is a prime number")
else: 
    print(f"{num} is a NOT prime number")