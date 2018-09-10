from reception.reception import vip,ordinary
def registrationCkecker(fnames):
    ordin = ordinary()
    VIP = vip()
    try:
        for name in VIP:
            fname = name[0]
            lname = name[1]
            if fnames.lower() == fname.lower():
                print ("Name : " + fnames + ' ' + lname +", Category: VIP")

    except expression as identifier:
        for name in ordin:
            fname = name[0]
            lname = name[1]
            if fnames.lower() == fname.lower():
                print ("Name : " + fnames + ' ' + lname +", Category: Ordinary")
            print("dsf")
    print("in")

registrationCkecker(fnames = input("Enter name: "))