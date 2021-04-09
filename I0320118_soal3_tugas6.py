
#program menentukan bilangan prima atau bukan prima

for angka in range(10,25):
    if angka > 1:
        for i in range(2,angka):
            if(angka % i == 0):
                print(angka, " bukan prima")
                break
        else:
            print(angka, " adalah bilangan prima")
    else:
        print(angka, "bukan prima")