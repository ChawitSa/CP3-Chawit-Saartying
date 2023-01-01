product = (("Cake","250"), ("Cola"," 18"), ("Water","  9"), ("Pizza","349"))

if input("Username: ") == "Admin" and input("Passcode: ") == "Passcode":
    print("\n======Welcome======")
    for i in range(len(product)):
        print(product[i][0],"\t",product[i][1],"\tBaht")
    no = int(input("select product[1-4]: "))
    if no>0 and no<5:
        amount = int(input("amount: "))
        print("\n"+product[no-1][0]," x ",amount," = ",amount*int(product[no-1][1]), "Baht")
    else:
        print("Try again later")
else:
    print("invalid account")
print("Bye Bye!!")