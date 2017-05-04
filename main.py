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

while(test1!=0 and test2!=0):

	player1draw=player1deck.TakeFromBottom()
	player1draw.displayCard()
	player2draw=player2deck.TakeFromBottom()
	player2draw.displayCard()
	better1=player1draw.checkRank()

	better2=player2draw.checkRank()
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
	print(test1)
	test2=player2deck.FindLength()
	print(test2)
