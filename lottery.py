import random
import matplotlib.pyplot as plt

account=0
a=[]
b=[]
for i in range(365):
    a.append(i+1)
    bet=random.randint(1,10)
    luckydraw=random.randint(1,10)

    if(bet==luckydraw):
        account=account+900-100
    else:
        account=account-100
    b.append(account)
print("Amount : ",account)
plt.plot(a,b)
plt.show()