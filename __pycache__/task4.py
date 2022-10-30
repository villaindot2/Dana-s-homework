

class Function:  
    def checking(self, list1):  
        return sorted(list1, key=len)


list = ["Google", "Apple", "Microsoft"]  

print(list)               
obj = Function()  
print(obj.checking(list))