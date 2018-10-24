#sumedh shingade
#54
#M



from random import randint as rt
def game(dice,faces):
    result=0
    for roll in range(0,dice):
        result+=rt(1,faces)
    result=game(2,6)
    print(result)
