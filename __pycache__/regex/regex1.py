import re


def is_valid(text):
    a = re.match("[0-9]{1,5}", text)  
    b = re.match("/W", text)
    c = re.match("/S", text)
    return a,b,c
        

a = is_valid("456345")
print(a)

# W - Возвращает совпадение, в котором строка НЕ содержит символов слова.
# S - Возвращает совпадение, в котором строка НЕ содержит символа пробела.
#