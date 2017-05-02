from __future__ import print_function
from deck import Deck
warDeck=Deck()
warDeck.Shuffle()
warDeck.Shuffle()
warDeck.Shuffle()
warDeck.Shuffle()
warDeck.Shuffle()
player1deck,player2deck = warDeck.Cut()
test1=player1deck.FindLength()
test2=player2deck.FindLength()
while(test1!=0 and test2!=0):

	player1draw=player1deck.TakeFromTop()

	player2draw=player2deck.TakeFromTop()

	better1=player1draw.checkRank()

	better2=player2draw.checkRank()

	test1=player1deck.FindLength()

	test2=player2deck.FindLength()

	if(better1>better2):
		player1deck.AddToBottom(player1draw)
		player1deck.AddToBottom(player2draw)

	if(better2>better1):
		player2deck.AddToBottom(player1draw)
		player2deck.AddToBottom(player2draw)

	if(better1==better2):
		player1deck.AddToBottom(player1draw)
		player2deck.AddToBottom(player2draw)
