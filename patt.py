for i in range (1,6):
    for j in range (1,i+1):
        if i==j or j==1 :
            print("*",end="");
        else :
            print(end=" ");
    for j in range (5,i,-1):
        print(end="  ")
    for j in range (1,i+1):
        if i==j or j==1 :
            print("*",end="");
        else :
            print(end=" ");
    print();
for i in range (5,0,-1):
    for j in range (1,i+1):
        if i==j or j==1 :
            print("*",end="");
        else :
            print(end=" ");
    for j in range (5,i,-1):
        print(end="  ")
    for j in range (1,i+1):
        if i==j or j==1 :
            print("*",end="");
        else :
            print(end=" ");
    print();
