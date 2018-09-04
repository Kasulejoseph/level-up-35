from reception.reception import vip,ordinary

def registrationCkecker(fnames):
    ordin = ordinary()
    VIP = vip()
    if not fnames or fnames.isspace() :
        return "Invalid input"
    else:
        for name in VIP:
            fname = name[0]
            lname = name[1]
            if fnames.lower() == fname or fnames.lower() ==lname:
                return "Name : " + fname + ' ' + lname +", Category: VIP"

        for name in ordin:
            fname = name[0]
            lname = name[1]
            if fnames.lower() == fname.lower() or fnames.lower() ==lname.lower():
                return "Name : " + fname + ' ' + lname +", Category: Ordinary"
        return "Not Registered"
print(registrationCkecker(fnames = input("Enter name: ")))
