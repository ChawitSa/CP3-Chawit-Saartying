n = int(input("n: "))
for i in range(n):
    for f in range(n-i-1):
        print(" ", end="")
    for f in range(2*i):
        print("*", end="")
    print("*")
print("Bye Bye!!")

if "J" in "HeolJ":
    print("Have")