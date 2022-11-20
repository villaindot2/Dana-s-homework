import re

# li = ['da','de','na']
# r = re.compile(".*a")
# filtered_list = list(filter(r.match, li))
# print(filtered_list)
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result

csv_gen = csv_reader("C:/Users/Dana/example.txt")

