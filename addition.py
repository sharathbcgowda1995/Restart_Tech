class Addition :
    def add(self,a,b):
        return a+b;

    def sub(self,c,d):
        if(c<d):
            print("enter the bigger number")
        else:
            return c-d;

obj=Addition()
result = obj.add(100,200)
print(result)

result = obj.sub(100,200)
if (result is not None):
    print(result)