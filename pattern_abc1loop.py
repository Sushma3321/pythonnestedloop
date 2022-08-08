i=0
while i<=5:
    j=0
    k=ord("A")+j
    while j<=i:
        print(chr(k+i),end="")
        k=k+1
        j=j+1
    print()
    i=i+1

