vowels=['a','e','i','o','u']

inp_str=input("Enter the string : ")
new_list=[]
for c in range(len(inp_str)):
    if inp_str[c] in vowels:
        new_list.append(inp_str[c])

     

print(f"The number of vowels in the given string are {len(set(new_list))}")