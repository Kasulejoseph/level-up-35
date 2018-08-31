from reception.reception import vip,ordinary

def registrationCkecker(fnames):
    ordin = ordinary()
    VIP = vip()
    for name in VIP:
        fname = name[0]
        lname = name[1]
        if fnames.lower() == fname:
            print ("Name : " + fname + ' ' + lname +", Category: VIP")
    print("invalid")
    for name in ordin:
        fname = name[0]
        lname = name[1]
        if fnames.lower() == fname.lower():
            print ("Name : " + fname + ' ' + lname +", Category: Ordinary")

registrationCkecker(fnames = input("Enter name: "))
