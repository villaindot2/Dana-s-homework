#Task2 1 вариант

class Function:  
    def checking(self, list1, n):
        
        if (n > 0):
            for i in range(n):
                b = type(list1[i]) 
                return b
        
#Назначаю длину листа
n = int(input("Print length of list"))
list = []

#Заполняю лист из консоли
if (n > 0):
    for i in range(n):
         a = input()
         list.append(a)
print(list)               
obj = Function()  
print(obj.checking(list,n))

####################################################################

#Task2 2 вариант

class Function:  
    def checking(self, list1):
        arr = []
        for i in range(3):
            
            arr.append(type(list1[i]))
        return arr
        

list = ["aa","b",456]
print(list)               
obj = Function()  
print(obj.checking(list))