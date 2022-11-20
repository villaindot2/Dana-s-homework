import re

# file = open('C:/Users/Dana/example.txt', 'r')
# re.search('SIS([\s\S]+?)Best', file)    
# with open('C:/Users/Dana/example.txt') as source, open('C:/Users/Dana/result.txt.txt', 'w') as destination:
#     for line in source:
#         if line.strip().endswith('_exec'):
#             destination.write(line)

# with open('C:/Users/Dana/example.txt') as f:
#     content = f.readlines()
# content = [x.strip() for x in content] 
file = open('C:/Users/Dana/example.txt')
li = file.readlines()
print(li)
a = re.search(('/(\SIS.*B)', li))
# data = file.read()
# data_into_list = data.replace('\n', ' ').split(".")

r = re.compile(".*BEST")
filtered_list = list(filter(r.match, li))

print(filtered_list)
# list = data_into_list
# print(list)


# file.close()

