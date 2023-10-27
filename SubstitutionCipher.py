import string
dict={}
data=""
fileop=open("66.txt","w")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print(dict)
with open("6.txt") as file:
    while(True):
        c=file.read(1)
        if not c:
            print("End of file")
            break
        if c in dict:
            data=dict[c] #print Substituted value
        else:
            data=c
        fileop.write(data)
        print(data,end="")
fileop.close()