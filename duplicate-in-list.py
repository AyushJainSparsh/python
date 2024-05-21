n=int(input("Number of element : "))
l=[]
for i in range (n):
    element=input("Enter the element : ")
    l.append(element)
print("List = ",l)
remove_duplicate_value=set(l)
print(remove_duplicate_value)