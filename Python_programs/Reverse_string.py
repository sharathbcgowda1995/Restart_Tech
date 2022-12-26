class Reverse:
    def reverse(self,name):
        rev_name=""
        length = len(name)
        print("Length of the string is : ", length)
        for i in range(length):
            rev_name=name[i]+rev_name
            print(rev_name)
        return rev_name

obj=Reverse()
name = obj.reverse(input("Enter any name : "))
print("Reversed name is : ", name)