def registrationCkecker(fnames):
    f = open("reception/vip.txt")
    ordinary = open("reception/ordinary_list.txt")
    for line in f:
        names = line.split()
        fname = names[0]
        lname = names[1]
        if fnames.lower() == fname.lower():
            print ("Name : " + fnames + ' ' + lname +", Category: VIP")
    for name in ordinary:
        names = name.split()
        fname = names[0]
        lname = names[1]
        if fnames.lower() == fname.lower():
            print ("Name : " + fnames + ' ' + lname +", Category: Ordinary")
    print("not found")
registrationCkecker(fnames = input("Enter name: "))
