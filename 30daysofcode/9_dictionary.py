n = int(input())
phoneBook = dict()
for i in range(n):
    entry = input().split()
    name, number = entry[0], entry[1]
    phoneBook[name] = number

query = input()
while query != "":
    if query in phoneBook:
        print(query,"=",phoneBook[query], sep = '')
    else:
        print("Not found")
    query = input()