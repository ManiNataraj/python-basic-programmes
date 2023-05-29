a=int(input("enter the a values: "));
b=int(input("enter the b values: "));
c=int(input("enter the c values: "));
if(b<a)&(a<c):
    print("a is  2nd biggest number",a);
elif(c>b)&(b>a):
    print("b is 2nd biggest number",b);
else:
    print("c is 2nd biggest number",c);
