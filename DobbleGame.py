# Find identical terms in list
import string
import random

symbol=list(string.ascii_letters)

list1=[0]*5
list2=[0]*5

pos1=random.randint(0,4)
pos2=random.randint(0,4)
print(pos1)
print(pos2)

samesymbol=random.choice(symbol)
symbol.remove(samesymbol)

if(pos1==pos2): #for same places
    list1[pos1]=samesymbol
    list2[pos1]=samesymbol
else: #for non-same places
    list1[pos1]=samesymbol
    list2[pos2]=samesymbol
    list1[pos2]=random.choice(symbol)
    symbol.remove(list1[pos2]) #so that the letter doesn't get repeated in next loop.
    list2[pos1]=random.choice(symbol)
    symbol.remove(list2[pos1]) #so that the letter doesn't get repeated in next loop.

# for places other than pos1 and pos2
i=0
while(i<5):
    if(i!=pos1 and i!=pos2):
        sym1=random.choice(symbol)
        symbol.remove(sym1)
        sym2=random.choice(symbol)
        symbol.remove(sym2)
        list1[i]=sym1
        list2[i]=sym2
    i+=1

print(list1)
print(list2)
