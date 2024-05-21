e = int(input("Enter size of list : "))
l=[]
for i in range(e):
    num = int(input("Enter element : "))
    l.append(num)
l.sort()
print("Sorted List : ",l)
key = int(input("Enter Key : "))
i=0
found = False
while i<=e :
    mid = (i+e)//2
    if l[mid]==key :
        found = True
        print(key," is found at ",mid," index")
        break
    elif l[mid]<key :
        i = mid+1
    else :
        e = mid-1
if not found :
    print(key," not found")