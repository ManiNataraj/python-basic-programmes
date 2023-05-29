number=int(input("how many terms? "));
n1,n2=0,1
count=0
if number<=0:
    print("please enter the positivenumber ")
elif number==1:
    print("fibonacci sequence upto",number,":");
    print(n1)
else:
    print("fibnocci sequence: ")
    while count<number:
        print(n1)
        number=n1+n2
        n1=n2
        n2=number
        count+=1
