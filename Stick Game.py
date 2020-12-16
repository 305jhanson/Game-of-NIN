# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 12:27:58 2020

@author: matt hanson
"""
import random

def printboard(board):
    stringboard=[0,0,0,0]
    strin=[]
    index=0
    total=0
    for num in board:
        total+=num
    if total==0:
        print("")
        return
    for nums in board:
        strin.append(index)
        for num in range(nums):
            strin.append("|")
        stringboard[index]=strin
        strin=[]
        index+=1
    for string in stringboard:
        print(*string)

def checkifgameover(board):
    total=0
    for num in board:
        total+=num
    if total==0:
        return True
    return False
def removebracket(board, row, amount):
    board[row]=board[row]-amount
    return board
def userinputremove(board):
    while True:
        row = int(input("what row would you like to remover from: "))
        if board[row]==0:
            print("row is empty")
            continue
        break
    while True:
        amount = int(input("how many sticks do you want to remove: "))
        if board[row]<amount:
            print("not enough sticks in row")
            continue
        break
    board = removebracket(board, row, amount)
    return board
def playgamehumanvhuman(games):
    player1wins=0
    player2wins=0
    for game in range(games):
        board=[7,5,3,1]
        gameover=False
        firstplayer=random.randint(0,1)
        if firstplayer==1:
             print("player 2 goes first")
             while True:
                printboard(board)
                print("player 2 pick options")
                board=userinputremove(board)
                printboard(board)
                gameover=checkifgameover(board)
                if gameover==True:
                    player1wins+=1
                    print("player 1 wins")
                if gameover==True:
                    break
                print("player 1 pick options")
                board=userinputremove(board)
                gameover=checkifgameover(board)
                if gameover==True:
                    player2wins+=1
                    print("player 2 wins")
                if gameover==True:
                    break
             print("player 1 wins: "+str(player1wins))
             print("player 2 wins: "+str(player2wins))
             print("")
        if firstplayer==0:
            print("player 1 goes first")
            while True:
                printboard(board)
                print("player 1 pick options")
                board=userinputremove(board)
                printboard(board)
                gameover=checkifgameover(board)
                if gameover==True:
                    player2wins+=1
                    print("player 2 wins")
                if gameover==True:
                    break
                print("player 2 pick options")
                board=userinputremove(board)
                gameover=checkifgameover(board)
                if gameover==True:
                    player1wins+=1
                    print("player 1 wins")
                if gameover==True:
                    break
            print("player 1 wins: "+str(player1wins))
            print("player 2 wins: "+str(player2wins))
            print("")
def playervcomputer(games,func):
    player1wins=0
    computerwins=0
    for game in range(games):
        board=[7,5,3,1]
        gameover=False
        firstplayer=random.randint(0,1)
        if firstplayer==1:
             print("computer goes first")
             while True:
                printboard(board)
                print("computer picking...")
                board=func(board)
                printboard(board)
                gameover=checkifgameover(board)
                if gameover==True:
                    player1wins+=1
                    print("Human wins")
                if gameover==True:
                    break
                print("Human pick options")
                board=userinputremove(board)
                gameover=checkifgameover(board)
                if gameover==True:
                    computerwins+=1
                    print("Computer wins")
                if gameover==True:
                    break
        if firstplayer==0:
            print("Human goes first")
            while True:
                printboard(board)
                print("Human pick options")
                board=userinputremove(board)
                printboard(board)
                gameover=checkifgameover(board)
                if gameover==True:
                    computerwins+=1
                    print("Computer wins")
                if gameover==True:
                    break
                print("Computer picking...")
                board=func(board)
                gameover=checkifgameover(board)
                if gameover==True:
                    player1wins+=1
                    print("Human wins")
                if gameover==True:
                    break
        print("human wins: "+str(player1wins))
        print("computer wins: "+str(computerwins))
        print("")
def computervcomputer(games,func1,func2):
    func1wins=0
    func2wins=0
    for game in range(games):
        board=[7,5,3,1]
        gameover=False
        firstplayer=random.randint(0,1)
        if firstplayer==1:
            print("func1 goes first")
            while True:
                board=func1(board)
                gameover=checkifgameover(board)
                if gameover==True:
                    func2wins+=1
                    print("function 2 wins")
                if gameover==True:
                    break
                board=func2(board)
                gameover=checkifgameover(board)
                if gameover==True:
                    func1wins+=1
                    print("function 1 wins")
                if gameover==True:
                    break
        if firstplayer==0:
            print("func2 goes first")
            while True:
                board=func2(board)
                gameover=checkifgameover(board)
                if gameover==True:
                    func1wins+=1
                    print("function 1 wins")
                if gameover==True:
                    break
                board=func1(board)
                gameover=checkifgameover(board)
                if gameover==True:
                    func2wins+=1
                    print("function 2 wins")
                if gameover==True:
                    break
        print("function 1 wins: "+str(func1wins))
        print("function 2 wins: "+str(func2wins))
        print("")
        
def bornLoser(board):
    row = board.index(max(board))
    board[row] = 0
    return board
def oneAtATime(state):
        for m in state:
            ind = state.index(m)
            if m > 0:    
                state[ind]=state[ind]-1
                return state    
        return state
    
def myfunction(board):
    def convertmultiple(num):
        lst_bin=[]
        if (num)//4!=0:
            lst_bin.append(4)
            num=num%4
        if (num>1):
            lst_bin.append(2)
            num=num%2
        if (num!=0):
            lst_bin.append(1)
        return lst_bin
    def nearend(board):
        rows=0
        for num in board:
            if num>0:
                rows+=1
        if rows==1:
            return True
        return False
    
    
    def isnimsum(board):
        index=0
        lst_mult=[[0],[0],[0],[0]]
        for num in board:
            number=num
            lst_mult[index]=convertmultiple(number)
            index+=1
        index=-1
        for lst in lst_mult:
            index+=1
            lst1=lst
            for num in lst1:
                for place in range(4):
                    if num in lst_mult[place] and index!=place:
                        lst_mult[place].remove(num)
                        lst_mult[index].remove(num)
                        break
        index0=0            
        for lst in lst_mult:
            if lst==[]:
                lst_mult[index0].append(0)     
            index0+=1
        return lst_mult
    
    def checkNim(board):
        mults=isnimsum(board)
        total=0
        isnim=False
        for lst in mults:
            for num in lst:
                total+=num
        if total==0:
            isnim=True
        if total>0:
            isnim=False
        return isnim
    
    
    end=nearend(board)
    total=0
    row=0
    if end==True:
        for index in range(4):
            if board[index]==1:
                board[index]=0
                return (board)
            if board[index]>1:
                board[index]=1
                return (board)
    for num in board:
        if num>0:
            row+=1
        total+=num
    if row==2:
        for num in range(4):
            if board[num]==1:
                for num in range(4):
                    if board[num]>1:
                        board[num]=0
                        return board
    if total==5 and row==4:
        for index1 in range(4):
            if board[index1]==2:
                board[index1]=0
                return board
    if total==3:
        for index in range(4):
            if board[index]==2:
                board[index]=0
                return board
    if row==4:
        num1=0
        for num in board:
            if num==1:
                num1+=1
        if num1==3:
            for index9 in range(4):
                if board[index9]>1:
                    board[index9]=0
                    return board
    if row==3:
        num1=0
        for num in board:
            if num==1:
                num1+=1
        if num1==2:
            for index9 in range(4):
                if board[index9]>1:
                    board[index9]=1
                    return board
    isnim=checkNim(board)
    if isnim==True:
        index=0
        for num in board:
            if num>0:
                board[index]=num-1
                return board
            index+=1
    if isnim==False:
        testboard=board
        index=-1
        for num in testboard:
            index+=1
            for number in range(1,num+1):
                newnum=num-number
                testboard[index]=newnum
                if checkNim(testboard)==True:
                    return testboard
                testboard[index]=newnum+number                
            
while True:
    print("welcome to stick game")
    players= int(input("how many human player want to play: "))
    if players==2:
        games=int(input("how many games do you want to play: "))
        playgamehumanvhuman(games)
    if players==1:
        games=int(input("how many games do you want to play: "))
        print("function options:")
        print("1. bornLoser")
        print("2. oneAtATime")
        print("3. myFunction")
        option= int(input("pick the number of the function: "))
        if option==1:
            playervcomputer(games,bornLoser)
        if option==2:
            playervcomputer(games,oneAtATime)
        if option==3:
            playervcomputer(games,myfunction)
    if players==0:
        games=int(input("how many games do you want to play: "))
        print("function options:")
        print("1. bornLoser")
        print("2. oneAtATime")
        print("3. myFunction")
        option1= int(input("pick the number of the function for function1: "))
        option2= int(input("pick the number of the function for function2: "))
        if option1==1:
            func1=bornLoser
        if option1==2:
            func1=oneAtATime
        if option1==3:
            func1=myfunction
        if option2==1:
            func2=bornLoser
        if option2==2:
            func2=oneAtATime
        if option2==3:
            func2=myfunction
        computervcomputer(games,func1,func2)
        

