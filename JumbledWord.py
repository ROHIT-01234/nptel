import random

def jumble():
    list_word=["superman","batman","wondarwomen","aquaman","flash","greenarrow","supergirl","shazam","greenlantern"]
    while("yes"):
        jumbled_word=random.choice(list_word) #Choose Random Word
        print("".join(random.sample(jumbled_word,len(jumbled_word))))#Shuffles the words
        x=input("What do you think what's the right word : ")
        if x==jumbled_word:
            print("Yep you're right it's ", x)
        else:
            print("Nah it's ",jumbled_word)
        c=input("What do you think?......Wanna give one more try(yes/no) : ")
        if c=="no":
            print("Nice playin with you....")
            break

if __name__=="__main__":
    jumble()