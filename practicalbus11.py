bus = [["a","a","a","a","a"],
        ["a","a","a","a","a"],
        ["a","a","a","a","a"],
        ["a","a","a","a","a"],
        ["a","a","a","a","a"]] 

for i in range(5):
    print(bus[i])

    row = int(input("Enter your row numder : "))
    seat = int(input("select your seat : "))

    if bus[row-1][seat-1]=="a":
        bus[row-1][seat-1]="r"
        print("Your seat is reserved")

    else:
        print("seat is already booked !!!")


        for i in range(5):
            print(bus[i])
