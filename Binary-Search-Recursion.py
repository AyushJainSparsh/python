def Search( l , key , e , i = 0) : 
    if i>=e :
        return -1
    mid = (i+e)//2
    if l[mid]==key :
        return mid
    elif l[mid]<key :
        return Search( l , key , e , mid+1 )
    else :
        return Search(  l , key , mid , i)

e = int(input("Enter size of list : "))
l=[5,8,6,4,2]

for i in range(e):
    num = int(input("Enter element : "))
    l.append(num)
l.sort()
print("Sorted List : ",l)
key = int(input("Enter Key : "))
f = Search( l , key , e , 0 )
if f==-1 :
    print(key," not Found")
else :
    print(key," is found at ",f," index")

