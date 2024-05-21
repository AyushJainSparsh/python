a = [8,2,6,4,5,7,3,9,1]
print(a)
def divide(l,i,e):
    if i<e :
        m = i + (e-i)//2
        divide(l,i,m)
        divide(l,m+1,e)
        l = conquer(l,i,m,e)
def conquer(l,i,m,e):
    s1,s2 = m-i+1 , e-m
    l1 = l[i:s1]
    l2 = l[m:s2]