#!/usr/bin/python3

import copy
import random

initialboard = None
sol = True
steps = 0
randRes = 0

class randomboardgenerator:
    def __init__(self, list=None):
        if list == None:
            self.randomboardgenerator = [["-" for i in range(0,n)] for j in range(0,n)]
            for j in range(0,n):
                rand_row = random.randint(0,n-1)
                if self.randomboardgenerator[rand_row][j] == "-":
                    self.randomboardgenerator[rand_row][j] = "Q"
            print("\nInitial placement of Queens on Chess Board:")
            printChessBoard(self.randomboardgenerator)

#This method prints the chess Board
def printChessBoard(st):
    for a in range(0,n):
          for b in range(0,n):
              if b < n-1:
                  print(st[a][b], end=" ")
              elif(b == n-1):
                  print(st[a][b], end="\n") 
                  

class solve:
    def __init__(self, option, sol):
        #intializing variables
        self.Runs = 1000
        self.Success = 0
        self.Fails = 0
        self.stepsSuccess = 0
        self.stepsFail = 0
        self.sideMoves = 0
        self.sol = sol
        
        if (option == 3):
            print("1. Without side moves\n2. With side moves\n")
            global x
            x = int(input())
        
        for i in range(0,1000):
            if self.sol == True:
                print ("\n************************")
                print ("Run #",i+1)
                print ("**************************")
            self.chessboard = randomboardgenerator(initialboard)
            self.costh = self.Heuristic(self.chessboard)
            #Calling the right variant of hill climbing
            if (option == 1):
                self.hillClimbing()
            elif (option == 2):
                self.hillclimbingwithsideways()
            elif (option == 3):
                self.randomRestart()

    #Simple Hill Climbing
    def hillClimbing(self):
        totalSteps = 0
        while 1:
            curattacks = self.costh
            if self.costh == 0:
                break
            self.bestBoard()
            if (curattacks == self.costh):
                self.Fails += 1
                self.stepsFail += totalSteps
                if totalSteps == 0:
                    self.stepsFail += 1
                break
            totalSteps += 1
            if self.sol == True:
                print ("\nThe Number of attack pairs is", (int)(self.Heuristic(self.chessboard)))
                printChessBoard(self.chessboard.randomboardgenerator)
            if (self.costh == 0):
                break
        if self.costh != 0:
            if self.sol == True:
                print ("\n======NO SOLUTION========")
        else:
            if self.sol == True:
                print ("\n======SOLUTION FOUND========")
            self.Success += 1
            self.stepsSuccess += totalSteps
        return self.costh
    
    #Hill Climbing Search with sideways moves
    def hillclimbingwithsideways(self):
        totalSteps = 0
        sideMoves = 0
        while 1:
            curattacks = self.costh
            curboard = self.chessboard
            if self.costh == 0:
                break
            self.nextBoard()
            if curboard == self.chessboard:
                self.stepsFail += totalSteps
                self.Fails += 1
                if totalSteps == 0:
                    self.stepsFail += 1
                break
            if curattacks == self.costh:
                sideMoves += 1
                if sideMoves == 100:
                    self.stepsFail += totalSteps
                    self.Fails += 1
                    break
            elif(curattacks > self.costh):
                sideMoves = 0
            totalSteps += 1
            if self.sol == True:
                print ("\nThe Number of attack pairs is", (int)(self.Heuristic(self.chessboard)))
                printChessBoard(self.chessboard.randomboardgenerator)
            if self.costh == 0:
                break
        if self.costh != 0:
            if self.sol == True:
                print ("\n=========NO SOLUTION==========")
        else:
            if self.sol == True:
                print ("\n==========SOLUTION FOUND===========")
            self.Success += 1
            self.stepsSuccess += totalSteps
        return self.costh
    
    #Random Restart Hill Climbing Search
    def randomRestart(self):
        global randRes
        global steps
        #Random Restart without sideways moves
        if x == 1:
            while 1:        
                curattacks = self.costh
                curboard = self.chessboard
                if self.costh == 0:
                    break
                self.bestBoard()
                if (curboard == self.chessboard) or ((curattacks == self.costh) & (self.costh != 0)):
                    self.chessboard = randomboardgenerator(initialboard)
                    randRes += 1 
                    self.costh = self.Heuristic(self.chessboard)               
                elif (self.costh < curattacks):  
                    if self.sol == True:
                        print ("\nAttack pairs:", (int)(self.Heuristic(self.chessboard)))
                        printChessBoard(self.chessboard.randomboardgenerator)
                steps += 1 
                if self.costh == 0:
                    break     
            if self.sol == True:
                print ("\n=========SOLUTION FOUND===========")
            self.Success += 1     
            return self.costh
        #Random Restart with sideways moves
        elif x == 2:
            sideMoves = 0
            while 1:
                curattacks = self.costh
                curboard = self.chessboard
                if self.costh == 0:
                    break
                self.nextBoard()
                if curboard == self.chessboard:
                    self.chessboard = randomboardgenerator(initialboard)
                    randRes += 1
                    self.costh = self.Heuristic(self.chessboard)
                if curattacks == self.costh:
                    sideMoves += 1
                    if sideMoves == 100:
                        self.chessboard = randomboardgenerator(initialboard)
                        randRes += 1
                        self.costh = self.Heuristic(self.chessboard)
                elif (curattacks > self.costh):
                    sideMoves = 0
                steps += 1
                if self.sol == True:
                    print ("\nAttack pairs:", (int)(self.Heuristic(self.chessboard)))
                    printChessBoard(self.chessboard.randomboardgenerator)
                if self.costh == 0:
                    break
            if self.sol == True:
                print("\n=========SOLUTION FOUND=============")
            self.Success += 1
            return self.costh
            
    #This function tries to shift each queen to each position with just one move and returns the move with the fewest attack pairs. 
    def bestBoard(self):
        mincost = self.Heuristic(self.chessboard)
        best_board = self.chessboard
        for acol in range(0,n):
            for arow in range(0,n):
                if self.chessboard.randomboardgenerator[arow][acol] == "Q":
                    for brow in range(0,n):
                        if self.chessboard.randomboardgenerator[brow][acol] != "Q":
                            temp = copy.deepcopy(self.chessboard)
                            temp.randomboardgenerator[arow][acol] = "-"
                            temp.randomboardgenerator[brow][acol] = "Q"
                            tempcost = self.Heuristic(temp)
                            if tempcost < mincost:
                                mincost = tempcost
                                best_board = temp
        self.chessboard = best_board
        self.costh = mincost

    #Finds the number of attack pairs
    def Heuristic(self, tempb):
        straight = 0
        diagonal = 0
        for i in range(0,n):
            for j in range(0,n):
                if tempb.randomboardgenerator[i][j] == "Q":
                    straight -= 2
                    for k in range(0,n):
                        if tempb.randomboardgenerator[i][k] == "Q":
                            straight += 1
                        if tempb.randomboardgenerator[k][j] == "Q":
                            straight += 1
                    k, l = i+1, j+1
                    while k < n and l < n:
                        if tempb.randomboardgenerator[k][l] == "Q":
                            diagonal += 1
                        k +=1
                        l +=1
                    k, l = i+1, j-1
                    while k < n and l >= 0:
                        if tempb.randomboardgenerator[k][l] == "Q":
                            diagonal += 1
                        k +=1
                        l -=1
                    k, l = i-1, j+1
                    while k >= 0 and l < n:
                        if tempb.randomboardgenerator[k][l] == "Q":
                            diagonal += 1
                        k -=1
                        l +=1
                    k, l = i-1, j-1
                    while k >= 0 and l >= 0:
                        if tempb.randomboardgenerator[k][l] == "Q":
                            diagonal += 1
                        k -=1
                        l -=1
        return ((diagonal + straight)/2)

    #Finds the successor board
    def nextBoard(self):
        count = 0
        que = {}
        currentcostt = self.Heuristic(self.chessboard)
        mincost = self.Heuristic(self.chessboard)
        best_board = self.chessboard
        for q_col in range(0,n):
            for q_row in range(0,n):
                if self.chessboard.randomboardgenerator[q_row][q_col] == "Q":
                    for m_row in range(0,n):
                        if self.chessboard.randomboardgenerator[m_row][q_col] != "Q":
                            test_board = copy.deepcopy(self.chessboard)
                            test_board.randomboardgenerator[q_row][q_col] = "-"
                            test_board.randomboardgenerator[m_row][q_col] = "Q"
                            test_board_cost = self.Heuristic(test_board)
                            if test_board_cost < mincost:
                                mincost = test_board_cost
                                best_board = test_board
                            if test_board_cost == currentcostt:
                                que[count] = test_board
                                count += 1
        if mincost == currentcostt:
            print("Successors with same heuristic value:", count)
            if(count == 1):
                best_board = que[0]  
            elif(count > 1):
                rand_ind = random.randint(0,count - 1)
                print("Successors with same heuristic value:", rand_ind)
                best_board = que[rand_ind]
        self.chessboard = best_board
        self.cost = mincost
        
    #Prints the output
    def printstats(self):
        if (option == 1) or (option == 2):
            print("Total number of Success: ", self.Success)
            print("Total number of Fails: ", self.Fails)
            print("Average of steps when it succeeds: ",self.stepsSuccess/self.Success)
            print("Average of steps when it fails: ", self.stepsFail/self.Fails)
            print("Success Rate: ", (self.Success/self.Runs)*100, "%")
            print("Failure Rate: ", (self.Fails/self.Runs)*100, "%")
        else:
            print("Number of Random Restarts: ", randRes)
            print("Average number of random resarts: ", randRes/self.Runs)
            print("Average number of steps: ", steps/self.Runs)

print("Enter number of queens: ")
n = int(input())
print("\nSelect the Search Strategy:\n1. Hill Climbing Search\n2. Hill Climbing Search with sideways moves\n3. Random restart hill climbing search\n")
option = int(input())

chessboard = solve(option, sol)
chessboard.printstats()
