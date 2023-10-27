def Magic_Square(n):
    magicsq = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        magicsq.append(l)

    i = n//2
    j = n-1

    num = n*n
    count = 1

    while(count<=num):
        if(i==-1 and j==n):
            i=0
            j=n-2
        else:
            if(j==n):
                j=0
            if(i==-1):
                i=n-1
        
        if(magicsq[i][j]!=0):
            j = j-2
            i = i+1
            continue
        else:
            magicsq[i][j]=count
            count+=1
        
        i = i-1
        j = j+1

    for i in range(n):
        for j in range(n):
            print(magicsq[i][j]," ",end="")
        print()

if __name__=="__main__":
    n=int(input("Give a Magic Squarw number :"))
    Magic_Square(n)
    print("Sum of rows/cloumns/diagonals in given Magic Square is ",n*(n**2+1)/2)
