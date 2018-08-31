list =[]
f = open("reception/vip.txt")
for line in f:
    for word in line:
    names = line.split()

# def vip():
#     list =[]
#     f = open("reception/vip.txt")
#     for line in f:
#         for word in line:
#         names = line.split()
#         # list.append(line)
#         fname = names[0]
#         lname = names[1]
#         print(names)
#         # return names

# def ordinary(fname,lname, category):
#     ordinary = open("reception/ordinary_list.txt")
#     for name in ordinary:
#         names = name.split()
#         fname = names[0]
#         lname = names[1]
#         return ordinary(fname,lname, category="Ordinary")