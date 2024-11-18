name=input("Enter a string: ")
rev_name=''.join(reversed(name))

if name==rev_name:
    print(f"{name} is a palindrome")
else:
    print(f"{name} is NOT a palindrome")