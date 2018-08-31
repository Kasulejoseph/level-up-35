def vip():
    list =[]
    f = open("reception/vip.txt")
    for line in f:
        word = [word.lower() for word in line.split()]
        list.append(word)
    return list

def ordinary():
    list =[]
    ordinary = open("reception/ordinary_list.txt")
    for line in ordinary:
        names = line.split()
        list.append(names)
    return list


