#Task1
#Создаю класс, в котором реализуется функция чек, проверяющая длину листа и количество повторений элемента
class Function:  
    def checking(self, list1):  
        return len(list1) < 1 or len(list1) == list1.count(list1[0]) 
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
print(obj.checking(list))