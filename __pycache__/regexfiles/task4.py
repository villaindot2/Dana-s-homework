names_list = [
'Emhyr var Emreis',
'Yennefer of Vengerberg',
'Philippa Eilhart',
'Cirilla Fiona Elen Riannon',
'Triss Merigold'
]

def Namelist(list):
    f1 = open('C:/Users/Dana/2.txt', 'w')
    for name in names_list:
        f1.write(name)
        f1.write('\n')
    f1.close()
    f1 = open('C:/Users/Dana/2.txt', 'r')
    return print(*f1)

print(Namelist(names_list))




