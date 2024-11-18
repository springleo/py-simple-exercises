sent1="I love Sandhya"
sent2="Sandhya love manu"

common_list=[]
# sent1_list=list(sent1)
for word in sent1.split():
    if word in sent2:
        common_list.append(word)
        # print(type(word))

print(common_list)

