while True :
    print("1.Add")
    print("2.Sub")
    print("3.Multiply")
    print("4.Divide")
    print("0.Exit")
    c=int(input("Enter Choice : "))
    if c==0 :
        break
    print("Enter numbers : ")
    n1,n2=float(input()),float(input())
    if c==1 :
        print("Add = ",n1+n2)
    elif c==2 :
        print("Subtract = ",n1-n2)
    elif c==3 :
        print("Multiply = ",n1*n2)
    elif c==4 :
        print("Divide = ",n1/n2)
    else :
        print("Enter valid choice")
