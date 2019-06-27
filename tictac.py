import sys

def check(a):
	#0,1,2
	#3,4,5
	#6,7,8
	if(a[0]==a[1]==a[2] and (a[0]=="X" or a[0]=="O")):
		if a[0]=="X":
			print("X Wins it")
		else:
			print ("O wins it")
		return True
	if(a[3]==a[4]==a[5] and (a[3]=="X" or a[3]=="O")):
		if a[3]=="X":
			print("X Wins it")
		else:
			print ("O wins it")
		return True
	if(a[6]==a[7]==a[8] and (a[6]=="X" or a[6]=="O")):
		if a[6]=="X":
			print("X Wins it")
		else:
			print ("O wins it")
		return True
	if(a[0]==a[3]==a[6] and (a[0]=="X" or a[0]=="O")):
		if a[0]=="X":
			print("X Wins it")
		else:
			print ("O wins it")
		return True
	if(a[1]==a[4]==a[7] and (a[1]=="X" or a[1]=="O")):
		if a[1]=="X":
			print("X Wins it")
		else:
			print ("O wins it")		
		return True
	if(a[2]==a[5]==a[8] and (a[2]=="X" or a[2]=="O")):
		if a[2]=="X":
			print("X Wins it")
		else:
			print ("O wins it")
		return True
	if(a[0]==a[4]==a[8] and (a[0]=="X" or a[0]=="O")):
		if a[0]=="X":
			print("X Wins it")
		else:
			print ("O wins it")
		return True
	if(a[2]==a[4]==a[6] and (a[2]=="X" or a[2]=="O")):
		if a[2]=="X":
			print("X Wins it")
		else:
			print ("O wins it")		
		return True

	return False
def init():
	board=[" "]*9
	return board

def select(a, s):
	g=int(input("Where would you like to place: "))
	while (g not in (range (0,9)) or (a[g]!=" ")):
		print("Please enter between 0,9")
		g=int(input("Where would you like to place: "))
	if s==0:
		a[g]="O"
	if s==1:
		a[g]="X"
	return a
def printb(board):
	print("   "+"|"+"   "+"|"+"   ")
	print(" "+(board[0])+" "+"|"+" "+(board[1])+" "+"|"+" "+(board[2])+" ")
	print(" 0 "+"|"+" 1 "+"|"+" 2 ")
	print("---"+"-"+"---"+"-"+"---")
	print("   "+"|"+"   "+"|"+"   ")
	print(" "+(board[3])+" "+"|"+" "+(board[4])+" "+"|"+" "+(board[5])+" ")
	print(" 3 "+"|"+" 4 "+"|"+" 5 ")
	print("---"+"-"+"---"+"-"+"---")
	print("   "+"|"+"   "+"|"+"   ")
	print(" "+(board[6])+" "+"|"+" "+(board[7])+" "+"|"+" "+(board[8])+" ")
	print(" 6 "+"|"+" 7 "+"|"+" 8 ")

def switchpalyer(player):
	if player == 0:
		return 1
	elif player == 1:
		return 0


#main
board = init()
player=0
printb(board)
print("")
print("")
print("")
while (check(board)==False):

	board=select(board, player)
	player=switchpalyer(player)
	printb(board)
	
	#if check(board)==True:
	#	break
	print("")
	print("")
	print("")





