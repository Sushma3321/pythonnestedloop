i=1
while i<=5:
    j=1
    while j<=5-i:
        print(" ",end=" ")
        j=j+1
    j=i
    while j>0:
        print(j,end=" ")
        j=j-1
    j=2
    while j<=i:
        print(j,end=" ")
        j=j+1
    print()
    i=i+1