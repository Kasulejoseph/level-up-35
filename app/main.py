from reception.reception import vip,ordinary

def registrationCkecker(fnames):
    ordin = ordinary()
    VIP = vip()
    for name in VIP:
        fname = name[0]
        lname = name[1]
        if fnames.lower() == fname:
            return "Name : " + fname + ' ' + lname +", Category: VIP"


    for name in ordin:
        fname = name[0]
        lname = name[1]
        if fnames.lower() == fname.lower():
            return "Name : " + fname + ' ' + lname +", Category: Ordinary"
    return "Not Registered"
print(registrationCkecker(fnames = input("Enter name: ")))
