from easygui import*
import sys
while 1:
    msgbox("e-bazaar")
    msg="from where you wanted to buy"
    title="welcome to online shopping"
    choices=["amazon","flipkart","jabong"]
    choice=choicebox(msg,title,choices)

    msgbox("you chose:"+str(choice),"survey result")

    msg="Do you want to continue?"
    title="please confirm"
    if ccbox(msg,title):    #show a continue/cancel dialog
        pass  #user chose continue
    else:
        sys.exit(0)
   

