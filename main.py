from __future__ import print_function
from deck import Deck

warDeck=Deck()
warDeck.Shuffle()
warDeck.Shuffle()
warDeck.Shuffle()
warDeck.Shuffle()
warDeck.Shuffle()
temporary=Deck()
temporary.EmptyDeck()
temporary2=Deck()
temporary2.EmptyDeck()

player1deck,player2deck = warDeck.Cut()
test1=player1deck.FindLength()
test2=player2deck.FindLength()
player1=raw_input("Enter Player 1's Name\n>")
print()
player2=raw_input("Enter Player 2's Name\n>")
print()

while(test1!=0 and test2!=0):
	
	player1draw=player1deck.TakeFromBottom()

	player2draw=player2deck.TakeFromBottom()

	better1=player1draw.checkRank()

	better2=player2draw.checkRank()
	userInput1=raw_input("{} hit enter to draw.\n>".format(player1))
	print()
	while(userInput1!=""):
		userInput1=raw_input("{} hit enter to draw.\n>".format(player1))
		print()
	if(userInput1==""):
		print("{} pulled a".format(player1),end=" ")
		player1draw.displayCard()
		print()
	userInput2=raw_input("{} hit enter to draw.\n>".format(player2))
	print()
	while(userInput2!=""):
		userInput2=raw_input("{} hit enter to draw.\n>".format(player2))
		print()
	if(userInput2==""):
		print("{} pulled a".format(player2),end=" ")
		player2draw.displayCard()
		print()
	templen=temporary.FindLength()
	templen2=temporary2.FindLength()

	if(better1>better2):
		player1deck.AddToBottom(player1draw)
		player1deck.AddToBottom(player2draw)
		
		if(templen!=0 and templen2!=0):
			while(templen!=0):
				card1=temporary.TakeFromBottom()
				card2=temporary2.TakeFromBottom()
				player1deck.AddToBottom(card1)
				player1deck.AddToBottom(card2)
				templen=temporary.FindLength()
				templen2=temporary2.FindLength()




	if(better2>better1):
		player2deck.AddToBottom(player1draw)
		player2deck.AddToBottom(player2draw)
		if(templen!=0 and templen2!=0):
			while(templen!=0):
				card1=temporary.TakeFromBottom()
				card2=temporary2.TakeFromBottom()
				player2deck.AddToBottom(card1)
				player2deck.AddToBottom(card2)
				templen=temporary.FindLength()
				templen2=temporary2.FindLength()
			
			


	if(better1==better2):
		temporary.AddToBottom(player1draw)
		temporary2.AddToBottom(player2draw)
	test1=player1deck.FindLength()

	test2=player2deck.FindLength()

	print("The score is {} to {} ({} to {})".format(test1,test2,player1,player2))
if(test1>test2):
	print("Congrats {}, you beat {}.".format(player1,player2))
else:
	print("Congrats {}, you beat {}.".format(player2,player1))