for i in range(0,4):
    for j in range(0,4-i):
        print(" ", end="")
    for k in range(0,2*i+1):
        print("*",end="")
    print()

for i in range(0,3):
    for j in range(0,3):
        print(" ", end="")
    for k in range(0,3):
        print("|",end="")
    print()
print("Success")

