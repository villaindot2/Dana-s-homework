


class Employee:
    def __init__(self, first_name = "Dana", last_name = "Omar"):
        self.first_name = first_name
        self.last_name = last_name
        
        

    def fullname(self):
        return self.first_name + " " + self.last_name
        
    def email(self):
        return self.first_name.lower()+"."+self.last_name.lower()+"@company.com"


obj = Employee() 
param = int(input("email or fullname?")) 

if param == 1:
    print(obj.email())
if param == 2:
    print(obj.fullname())

