a=int(input("enter the value: "))
for num in range(a):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
