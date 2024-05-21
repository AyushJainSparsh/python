print("Enter Marks : ");
a,b,c,d,e=float(input()),float(input()),float(input()),float(input()),float(input());

per=(a+b+c+d+e)/5;
print("Percentage = ",per);
if per>75 :
    print("Pass with 1st division");
elif per>50 :
    print("Pass with 2nd division");
elif per>35 :
    print("Pass with 3rd division");
else :
    print("Fail");