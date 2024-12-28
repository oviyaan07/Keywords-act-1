string=input("enter a word ")
flag=0
for i in string:
    if i=='A' or i=='a':
        flag=1
        break
if flag==1:
    print("a is found")
else:
    print("a is not found")