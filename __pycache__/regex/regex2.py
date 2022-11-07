import re
def letters_only(text):
    a = re.findall('[a-zA-Z]', text)
    return ''.join(a)
    print(a)

print(letters_only("R!=:~0o0./c&}9k`60=y") )

#[a-zA-Z] Возвращает совпадение для любого символа в алфавитном порядке между a и z, в нижнем регистре ИЛИ в верхнем регистре.
#Возвращает список, содержащий все совпадения