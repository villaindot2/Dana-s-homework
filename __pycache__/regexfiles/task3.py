def Lines(file):
    with file as files:
        list = [string.rstrip() for string in files]
    print(list)
file = open('C:/Users/Dana/1.txt')
print(Lines(file))