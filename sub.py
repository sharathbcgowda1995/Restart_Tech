class Addition :
    def sub(self,c,d):
        if(c<d):
            print("enter the bigger number")
        else:
            return c-d;

obj=Addition()
result = obj.sub(500,200)
if (result is not None):
    print(result)