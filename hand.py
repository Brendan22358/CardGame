from card import Card

class Hand:
	def __init__(self):
		self.firstcard=Card("9","clubs")
		self.player1hand=[]
		self.player2hand=[]
		for i in range (1,27):
			self.player1hand.append(i)
		for i in range (27,53):
			self.player2hand.append(i)
		for card1 in self.player2hand:
			pass
		print(self.player1hand)
		print(self.player2hand)
		self.firstcard.displayCard()
