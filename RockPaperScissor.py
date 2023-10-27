def rps(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    print(p1,p2)
    if(player1[p1]==player2[p2]):
        print("Draw!!")
    elif(player1[p1]=="Rock" and player2[p2]=="Paper"):
        print("Player2 wins!")
    elif(player1[p1]=="Rock" and player2[p2]=="Scissor"):
        print("Player1 wins!")
    elif(player1[p1]=="Scissor" and player2[p2]=="Paper"):
        print("Player1 wins!")
    elif(player1[p1]=="Paper" and player2[p2]=="Rock"):
        print("Player1 wins!")
    elif(player1[p1]=="Scissor" and player2[p2]=="Rock"):
        print("Player2 wins!")
    elif(player1[p1]=="Paper" and player2[p2]=="Scissor"):
        print("Player2 wins!")


player1={0:"Rock",1:"Paper",2:"Scissor"}
player2={0:"Paper",1:"Rock",2:"Scissor"}
while("yes"):
    num1=input("Player1, Enter Your Choice : ")
    num2=input("Player2, Enter Your Choice : ")
    bit1=int(input("Player1 Enter your bit choice : "))
    bit2=int(input("Player2 Enter your bit choice : "))
    rps(num1,num2,bit1,bit2)
    ch=input("Want to Continue ? (yes/no) : " )
    if(ch=="no"):
        break
