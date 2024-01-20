import random
print("::: Lets play Rock Paper sissors ::")
while True:
        
        print("")
        print (":: Best of 3 ::")
        i=0
        comp=0
        pla=0
        while(i<3):
            computer=["rock", "paper", "sissors"]
            cch=random.choice(computer)
            print("")
            player1=input("Enter your choice: ")
            player1=player1.lower()
            print("Computer's choise is: %s" %cch)
            if(player1==cch):
                print("Draw")
                comp=comp+1
                pla=pla+1
            elif(cch=="rock" and player1=="sissors"):
                print("::Computer scored::")
                comp=comp+1
            elif(cch=="paper" and player1=="rock"):
                print("::Computer scored::")
                comp=comp+1
            elif(cch=="sissors" and player1=="paper"):
                print("::Computer scored::")
                comp=comp+1
            elif(cch=="rock" and player1=="paper"):
                print("::You scored::")
                pla=pla+1
            elif(cch=="paper" and player1=="sissors"):
                print("::You scored::")
                pla=pla+1
            elif(cch=="sissors" and player1=="rock"):
                print("::You scored::")
                pla=pla+1
            i=i+1
        
        if(comp>pla):
            print("")
            print("Your score : %d \n Computer score : %d"%(pla,comp))
            print(":: Over all champion Computer::")
        elif(comp<pla):
             print("")
             print("Your score : %d \n Computer score : %d"%(pla,comp))
             print("::Over all champion You ::")
        elif(comp==pla):
            print("")
            print("Your score : %d \n Computer score : %d"%(pla,comp))
            print("::Opps the overll match has been drawed ::")
        print("")
          
        ch=input("Do you wnat to play again[y/n]?")
        if(ch.lower()=="n"):
            print("")
            print(":::: Thanks for playing with us ::::")
            print("")
            break
