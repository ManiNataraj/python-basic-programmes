class ob:
    def fun(self,a,b):
        self.a=a
        self.b=b
        print("The value is:");
        
    def fun1(self):
        c=self.a+self.b;
        print(c);

obj=ob();
obj.fun(1000,2000);
obj.fun1();
