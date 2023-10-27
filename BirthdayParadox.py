import random
import datetime
birthday=[]
i=0
while(i<50):
    y=random.randint(1800,2020)
    if(y%4==0 and y%100!=0 or y%400==0):
        leap=1
    else:
        leap=0

    m=random.randint(1,12)
    if(m==2 and leap==1):
        d=random.randint(1,29)
    elif(m==2 and leap==0):
        d=random.randint(1,29)
    elif(m==4 or m==6 or m==9 or m==11):
        d=random.randint(1,30)
    else:
        d=random.randint(1,31)
    dd=datetime.date(y,m,d)
    day_of_year=dd.timetuple().tm_yday
    i+=1
    birthday.append(day_of_year)
birthday.sort()
j=0
while(j<50):
    """ if(birthday[j]==birthday[j+1]):
        print("[",birthday[j],"--",birthday[j+1],"]")
    else: """
    print(birthday[j])
    j+=1


