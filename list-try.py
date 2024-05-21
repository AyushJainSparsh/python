language=[52,3.25,"Hello "];# mutable-can be changed
add=[48,1.75,"World"];
for i in range (0,3):
    print(language[i]+add[i],end=" ");
print();
add.remove;
for i in range (0,3):
    print(add[i],end="\t");
print();
add[1]=54;
for i in range (0,3):
    print(add[i],end="\t");
print();

touple=4,5,8.5;# immutable-cannot be changed

for i in range (0,3):
    print(touple[i],end="\t");
print();
