import re
def letters_only(text):
    a = re.findall('[a-zA-Z]', text)
    print(a)

print(letters_only("R!=:~0o0./c&}9k`60=y") )